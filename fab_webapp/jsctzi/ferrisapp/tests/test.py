import os
import unittest

from flask_appbuilder import SQLA
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.tests import test_api
from flask_appbuilder.tests.sqla.models import Model1
from flask_appbuilder.tests.test_menu import FlaskTestCase


class FT(FlaskTestCase):
    def setUp(self):
        from flask import Flask
        from flask_appbuilder import AppBuilder
        from flask_appbuilder.views import ModelView

        self.app = Flask(__name__)
        self.basedir = os.path.abspath(os.path.dirname(__file__))
        self.app.config.from_object("flask_appbuilder.tests.config_api")
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:Gabarek90125@ferris-postgres/ferris_ef"
        self.app.config["FAB_API_MAX_PAGE_SIZE"] = 10

        self.db = SQLA(self.app)
        self.appbuilder = AppBuilder(self.app, self.db.session)

        class Model1View(ModelView):
            datamodel = SQLAInterface(Model1)

        self.appbuilder.add_view(Model1View, "Model1")


if __name__ == "__main__":
    ft = FT()

    ft.setUp()
    ft.test_menu_access_denied()
    ft.test_menu_api()
    ft.tearDown()

    # ft = test_api.APITestCase()
    #
    # ft.test_auth_login_bad()

    print("Everything passed")
