"""
Module for configuring and initializing the FerrisApp application.

This module sets up the necessary configurations for the FerrisApp application, including logging, database, and
Flask extensions.

Classes:
    - FerrisAppBuilder: Custom class for initializing the FerrisApp application.

Functions:
    - get_appbuilder: Getter function for accessing the appbuilder variable.

Imports:
    - logging: The logging module for configuring the application's logging settings.
    - os: The os module for accessing environment variables.
    - ssl: The ssl module for creating SSL/TLS contexts.
    - flask_appbuilder.SQLA: The SQLA class from the flask_appbuilder module for managing the database.
    - flask_multistatic.MultiStaticFlask: The MultiStaticFlask class from the flask_multistatic module for serving
        static files.
    - ferrisapp.app.views.index.FerrisIndexView: The FerrisIndexView class from the ferrisapp.app.views.index module
        for defining the index view.
    - .base.FerrisAppBuilder: The FerrisAppBuilder class from the .base module for customizing the app initialization.

Variables:
    - app: The Flask application object.
    - db: The SQLA object for managing the database.
    - migrate: The Migrate object for handling database migrations.
    - appbuilder: The FerrisAppBuilder object for initializing the FerrisApp application.

"""

import base64
import json
import logging
import os
import ssl
from typing import Any

from ferrisapp.app.views.index import FerrisIndexView
from flask_appbuilder import SQLA
from flask_multistatic import MultiStaticFlask

from .base import FerrisAppBuilder

APP_THEME_CONFIG_KEY = "APP_THEME"


def get_appbuilder():
    """
    Getter function for accessing the appbuilder variable, since the API add-on needs to access it and this avoids a
    circular import

    Returns:
        The appbuilder object for initializing the FerrisApp application.
    """
    return appbuilder


def decode_dictionary(encoded_input_string: str) -> dict[str, Any]:

    deco = base64.b64decode(encoded_input_string).decode("utf-8")  # str
    json_dict = json.loads(deco)  # dict

    return json_dict


ssl._create_default_https_context = ssl._create_unverified_context

"""
 Logging configuration
"""

app = MultiStaticFlask(__name__)


app.config.update(dict(os.environ))

if os.environ.get("CONSUL_HOST", None):
    # Override default configuration with one loaded from consul
    app.config.from_mapping(FerrisAppBuilder.get_config())


with open("/etc/creds-volume/secrets.json", "r") as fin:
    content = fin.read()
    extra_conf_dict = json.loads(content)
    app.config.update(extra_conf_dict)


logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(app.config.get("LOGGING_LEVEL", 10))
logging.getLogger("elasticsearch").disabled = True
logging.getLogger("kafka").setLevel(logging.ERROR)

app.config[APP_THEME_CONFIG_KEY] = (
    app.config[APP_THEME_CONFIG_KEY] + ".css" if APP_THEME_CONFIG_KEY in app.config else "ferris.css"
)

if app.config.get("DB_HOST", None):
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql://{app.config['DB_USERNAME']}:{app.config['DB_PASSWORD']}@"
        f"{app.config['DB_HOST']}:{app.config['DB_PORT']}/{app.config['DB_NAME']}"
    )


db = SQLA(app)

from flask_migrate import Migrate

migrate = Migrate(app, db, compare_type=True)

from ferrisapp.app.manager import FerrisSecurityManager

appbuilder = FerrisAppBuilder(
    app=app,
    session=db.session,
    base_template="ferris/baselayout.html",
    indexview=FerrisIndexView(),
    security_manager_class=FerrisSecurityManager,
)


from .views import views_loader
