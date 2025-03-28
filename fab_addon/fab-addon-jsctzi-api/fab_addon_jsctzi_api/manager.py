# File auto generated, DO NOT edit because it will be smashed

import logging

from flask_appbuilder.basemanager import BaseManager
from flask_babel import lazy_gettext

from .views.user_account import JSCTZIUserAccountView
from .views.address import JSCTZIAddressView


log = logging.getLogger(__name__)

"""
   Create your plugin manager, extend from BaseManager.
   This will let you create your models and register your views.

"""


class JSCTZIManager(BaseManager):
    def __init__(self, appbuilder):
        """
        Use the constructor to setup any config keys specific for your app.
        """
        super().__init__(appbuilder)

    def register_views(self):
        """
        This method is called by AppBuilder when initializing, use it to add your views
        """

        self.appbuilder.add_view(
            JSCTZIUserAccountView,
            "User Account",
            label=lazy_gettext("User Account"),
            href="/user_account/list/",
            
            
            
            
        )
        self.appbuilder.add_view(
            JSCTZIAddressView,
            "Address",
            label=lazy_gettext("Address"),
            href="/address/list/",
            
            
            
            
        )

    def pre_process(self):
        pass

    def post_process(self):
        pass
