"""
Module for defining the FerrisAppBuilder class and related functions.

This module provides the FerrisAppBuilder class, which is a subclass of the AppBuilder class from flask_appbuilder.
It also includes several related functions for configuring the FerrisApp application.

Classes:
    - FerrisAppBuilder: Subclass of AppBuilder for initializing the FerrisApp application.

Functions:
    - str_to_dict: Custom filter function for converting a string to a dictionary.
    - apply_templates: Static method for applying templates to a modelview.
    - get_config: Static method for getting the application configuration.
    - add_view: Method for adding a view to the application.
    - add_view_no_menu: Method for adding a view to the application without including it in the menu.
    - register_event_handler: Method for registering an event handler.
    - app_name: Property for getting the application name.
    - _load_addon_translations: Private method for loading addon translations.
    - _set_addon_static_folders: Private method for setting addon static folders.

Imports:
    - importlib: The importlib module for importing addon modules.
    - os: The os module for accessing file paths and directories.
    - ferris_cli.v2.ApplicationConfigurator: The ApplicationConfigurator class from the ferris_cli.v2 module.
    - flask_appbuilder.AppBuilder: The AppBuilder class from the flask_appbuilder module.
    - jinja2.Environment: The Environment class from the jinja2 module for managing templates.
    - jinja2.PackageLoader: The PackageLoader class from the jinja2 module for loading templates from packages.
    - jinja2.select_autoescape: The select_autoescape function from the jinja2 module for autoescaping templates.
    - jinja2.ChoiceLoader: The ChoiceLoader class from the jinja2 module for loading templates from multiple loaders.
    - .services.broker.FerrisBroker: The FerrisBroker class from the .services.broker module for handling broker
        configurations.
    - .views.Templates: The Templates class from the .views module for applying templates.
    - .views.Widgets: The Widgets class from the .views module for applying widgets.

Variables:
    - DEFAULT_BROKER: Default value for the broker configuration.
    - environments: Dictionary for caching Jinja2 environments for addon packages.
    - registered_event_handlers: Dictionary for caching registered event handlers.
"""

import importlib
import os

from ferris_cli.v2 import ApplicationConfigurator
from flask_appbuilder import AppBuilder
from jinja2 import ChoiceLoader, Environment, PackageLoader, select_autoescape

from .filters import str_to_dict
from .services.broker import FerrisBroker
from .views import Templates, Widgets


class FerrisAppBuilder(AppBuilder):
    """
    Subclass of AppBuilder for initializing the FerrisApp application.

    This class extends the AppBuilder class from flask_appbuilder to provide additional functionality specific to the
    FerrisApp application.

    Attributes:
        - environments (dict): Dictionary for caching Jinja2 environments for addon packages.
        - registered_event_handlers (dict): Dictionary for caching registered event handlers.
        - DEFAULT_BROKER (str): Default value for the broker configuration.

    Methods:
        - __init__(self, **kwargs): Initializes the FerrisAppBuilder object.
        - get_env(self, package_name=None): Returns the Jinja2 environment for the specified package.
        - apply_templates(modelview): Applies templates to the specified modelview.
        - get_config(): Returns the application configuration.
        - get_default_broker(self): Returns the default broker configuration.
        - add_view(self, baseview, name, href="", icon="", label="", category="", category_icon="", category_label=""):
            Adds a view to the application.
        - add_view_no_menu(self, baseview, endpoint=None, static_folder=None): Adds a view to the application without
            including it in the menu.
        - register_event_handler(self, events, handler_class): Registers an event handler for the specified events.
        - app_name(self): Property for getting the application name.
        - _load_addon_translations(self, app): Loads addon translations for the application.
        - _set_addon_static_folders(self, app): Sets addon static folders for the application.
    """

    environments = {}
    registered_event_handlers = {}

    DEFAULT_BROKER = "kafka"

    def __init__(self, **kwargs):
        _app = kwargs.get("app")

        # Doing this to put security menu item to the bottom, after all addon views are loaded
        _tmp_fab_add_security_views = _app.config.get("FAB_ADD_SECURITY_VIEWS", True)
        _app.config["FAB_ADD_SECURITY_VIEWS"] = False

        self._load_addon_translations(_app)
        self._set_addon_static_folders(_app)

        super().__init__(**kwargs)

        # Doing this to put security menu item to the bottom, after all addon views are loaded
        _app.config["FAB_ADD_SECURITY_VIEWS"] = _tmp_fab_add_security_views

        self.sm.register_views()

        self.get_app.default_broker = FerrisBroker(self.get_app.config.get("DEFAULT_BROKER", self.DEFAULT_BROKER))

    def get_env(self, package_name=None):
        """
        Returns the Jinja2 environment for the specified package.
        This method checks if the package is imported and creates a Jinja2 environment with the package's templates.
        It also adds the custom filter "str_to_dict" and updates filters and globals from the application's Jinja2
        environment.

        Args:
            package_name (str): The name of the package.

        Returns:
            Jinja2 Environment: The Jinja2 environment for the specified package.
        """
        if package_name:
            package_name = package_name.split(".")[0]

            if importlib.find_loader(package_name):
                if self.environments.get(package_name, None):
                    return self.environments.get(package_name)

                addon_loader = PackageLoader(package_name, "templates")
                app_loader = self.app.jinja_env.loader

                env = Environment(
                    loader=ChoiceLoader([addon_loader, app_loader]), autoescape=select_autoescape(["html", "xml"])
                )

                self.app.jinja_env.filters["str_to_dict"] = str_to_dict
                env.filters.update(self.app.jinja_env.filters)
                env.globals.update(self.app.jinja_env.globals)

                return env

        return self.app.jinja_env

    @staticmethod
    def apply_templates(modelview):
        """
        This is a static method that applies templates from the Templates class and widgets from the Widgets class to
        the modelview.

        Args:
            modelview: The modelview to apply templates to.
        """
        Templates.apply_modelview_templates(modelview)
        Widgets.apply_widgets(modelview)

    @staticmethod
    def get_config():
        """
            This is a static method that calls the get() method of the ApplicationConfigurator class to obtain the
            application configuration.

        Returns:
            dict: The application configuration obtained from the ApplicationConfigurator.
        """
        return ApplicationConfigurator().get()

    def get_default_broker(self):
        """
        Returns the default broker configuration.

        Returns:
            str: The default broker configuration obtained from the application's default_broker attribute.

        """
        return self.get_app.default_broker

    def add_view(
        self,
        baseview,
        name,
        href="",
        icon="",
        label="",
        category="",
        category_icon="",
        category_label="",
    ):
        """
        Adds a view to the application.

        Args:
            baseview: The baseview to add.
            name (str): The name of the view.
            href (str, optional): The href URL of the view. Defaults to "".
            icon (str, optional): The icon class of the view. Defaults to "".
            label (str, optional): The label of the view. Defaults to "".
            category (str, optional): The category of the view. Defaults to "".
            category_icon (str, optional): The icon class of the category. Defaults to "".
            category_label (str, optional): The label of the category. Defaults to "".

        Returns:
            View: The added view.

        Note:
            This method adds a view to the application using the provided arguments.
            If the application is in "WORKER_MODE", the view will not be added and None will be returned.

        """
        if not self.get_app.config.get("WORKER_MODE", False):
            return super().add_view(
                baseview=baseview,
                name=name,
                href=href,
                icon=icon,
                label=label,
                category=category,
                category_icon=category_icon,
                category_label=category_label,
            )

        return

    def add_view_no_menu(self, baseview, endpoint=None, static_folder=None):
        """
        Adds a view to the application without including it in the menu.

        Args:
            baseview: The baseview to add.
            endpoint (str, optional): The endpoint URL of the view. Defaults to None.
            static_folder (str, optional): The static folder path of the view. Defaults to None.

        Returns:
            View: The added view.

        Note:
            This method adds a view to the application without including it in the menu.
            If the application is in "WORKER_MODE", the view will not be added and None will be returned.

        """
        if not self.get_app.config.get("WORKER_MODE", False):
            return super().add_view_no_menu(baseview=baseview, endpoint=endpoint, static_folder=static_folder)

        return

    def register_event_handler(self, events, handler_class):
        """
        Registers an event handler for the specified events.

        Args:
            events (list): List of events to register the handler for.
            handler_class: The event handler class to register.

        Note:
            This method registers an event handler for the specified events.
            If the application is in "WORKER_MODE", the event handler will not be registered.

        """
        if self.get_app.config.get("WORKER_MODE", False):
            for event in events:
                if not event in self.registered_event_handlers:
                    self.registered_event_handlers[event] = []

                self.registered_event_handlers[event].append(handler_class)

    @property
    def app_name(self):
        """
        Get the App name

        :return: String with app name
        """
        return self.get_app.config["APP_TITLE"]

    def _load_addon_translations(self, app):
        """
        Loads addon translations for the application.

        Args:
            app: The Flask application object.

        Note:
            This method loads translations for addons registered in the application.
            It searches for translation directories in each addon package and adds them to the Babel translation
            directories.

        """
        trans = app.config.get("BABEL_TRANSLATION_DIRECTORIES", "")

        for addon in app.config.get("ADDON_MANAGERS"):
            addon_name = addon.split(".")[0]
            module = importlib.import_module(addon_name)
            addon_trans_dir = f"{module.__file__.rsplit('/', 1)[0]}/translations"

            if os.path.exists(addon_trans_dir):
                trans += f";{addon_trans_dir}"

        app.config["BABEL_TRANSLATION_DIRECTORIES"] = trans.lstrip(";")

    def _set_addon_static_folders(self, app):
        """
        Sets static folders for addons in the application.

        Args:
            app: The Flask application object.

        Note:
            This method sets the static folder paths for addons registered in the application.
            It searches for static directories in each addon package and adds them to the static folder list of the
            application.

        """
        static_folder = []

        for addon in app.config.get("ADDON_MANAGERS"):
            addon_name = addon.split(".")[0]
            module = importlib.import_module(addon_name)
            addon_static_dir = f"{module.__file__.rsplit('/', 1)[0]}/static"

            if os.path.exists(addon_static_dir):
                static_folder.append(addon_static_dir)

        static_folder.append(os.path.join(app.root_path, "static"))
        app.static_folder = static_folder
