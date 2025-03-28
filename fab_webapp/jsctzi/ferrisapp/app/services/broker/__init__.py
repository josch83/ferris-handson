import logging

from .kafka import FerrisKafka


class FerrisBroker:
    def __init__(self, broker=None, is_json=True):
        self.instance = FerrisKafka(is_json)

    def send(self, topic, message):
        resp = self.instance.send(topic, message)

        logging.getLogger("ferris.app.broker").debug("TOPIC: %s", topic)
        logging.getLogger("ferris.app.broker").debug("MESSAGE: %s", message)
        logging.getLogger("ferris.app.broker").debug("RESPONSE: %s", resp)

        return resp
