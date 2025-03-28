import json

from ferris_cli.v2 import ApplicationConfigurator
from ferris_cli.v2.services.config import DEFAULT_CONFIG
from kafka import KafkaProducer

"""
class FerrisKafka:
    def __init__(self, is_json=True):
        config = ApplicationConfigurator().get()
        broker_address = f"{config['KAFKA_BOOTSTRAP_SERVER']}:{config['KAFKA_PORT']}"

        self._is_json = is_json

        if is_json:
            self.producer = KafkaProducer(
                bootstrap_servers=broker_address, value_serializer=lambda x: json.dumps(x).encode("utf-8")
            )
        else:
            self.producer = KafkaProducer(bootstrap_servers=broker_address)

    def send(self, topic, message):
        resp = self.producer.send(topic, message)

        return resp
"""


class FerrisKafka:

    def __init__(self, host=None, port=None, is_json=True):
        conf = ApplicationConfigurator.get(DEFAULT_CONFIG)

        if host and port:
            broker_address = f"{host}:{port}"
        else:
            broker_address = f"{conf.get('KAFKA_BOOTSTRAP_SERVER')}:{conf.get('KAFKA_PORT')}"

        self._is_json = is_json

        value_serializer = None if not is_json else lambda x: json.dumps(x).encode("utf-8")

        self.producer = KafkaProducer(
            api_version="3.6.1",
            security_protocol="SSL",
            ssl_cafile="/usr/local/lib/python3.11/site-packages/certifi/cacert.pem",
            ssl_certfile="/usr/local/lib/python3.11/site-packages/certifi/cacert.pem",
            bootstrap_servers=broker_address,
            value_serializer=value_serializer,
            max_request_size=10485760,
        )

    def send(self, topic, message):

        resp = self.producer.send(topic, message).get()

        return resp
