import os

from ferris_cli.v2 import ApplicationConfigurator


def set_test_envs():
    os.environ["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:Gabarek90125@dev-postgres/ferrisweb"
