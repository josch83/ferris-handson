import logging
import os
import ssl

from ferrisapp import config
from ferrisapp.app.base import FerrisAppBuilder
from ferrisapp.app.views.index import FerrisIndexView
from ferrisapp.tests import test_config
from ferrisapp.tests.const import (
    MODEL1_DATA_SIZE,
    PASSWORD_ADMIN,
    PASSWORD_READONLY,
    TEMPLATES_FOLDER,
    USERNAME_ADMIN,
    USERNAME_READONLY,
)
from flask import Flask
from flask_appbuilder import SQLA
from flask_appbuilder.tests.base import FABTestCase

ssl._create_default_https_context = ssl._create_unverified_context

template_dir = os.path.abspath(TEMPLATES_FOLDER)
app = Flask(__name__, template_folder=template_dir)


app.config.from_object(config)
app.config.update(dict(os.environ))

app.config.from_mapping(FerrisAppBuilder.get_config())


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://{}:{}@{}:{}/{}".format(
    app.config["DB_USERNAME"], app.config["DB_PASSWORD"], app.config["DB_HOST"], app.config["DB_PORT"], "test"
)

db = SQLA(app)

from flask_migrate import Migrate

migrate = Migrate(app, db)

from ferrisapp.app.manager import FerrisSecurityManager

appbuilder = FerrisAppBuilder(
    app=app,
    session=db.session,
    base_template="ferris/baselayout.html",
    indexview=FerrisIndexView(),
    security_manager_class=FerrisSecurityManager,
)


class FerrisTestBase(FABTestCase):
    def setUp(self):
        self.app = app

        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger().setLevel(app.config.get("LOGGING_LEVEL", 10))

        self.db = SQLA(self.app)
        self.appbuilder = appbuilder

        self.client = self.app.test_client()
