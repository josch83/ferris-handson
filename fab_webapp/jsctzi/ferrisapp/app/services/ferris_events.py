from ferris_cli.v2.services.events import FerrisEvents as FE
from ferrisapp.app import app


class FerrisEvents(FE):
    def __init__(self, broker=None):
        super().__init__()

        self.broker = broker if broker else app.default_broker
