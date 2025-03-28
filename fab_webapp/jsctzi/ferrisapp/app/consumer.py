"""
This module defines a Faust application for event processing.

It imports the necessary dependencies and sets up a Faust application with a broker connection.
It also defines an `Event` class to represent event records and creates a topic for events.

The `process` function is an async agent that processes events received from the topic.
It iterates over registered event handlers and triggers them for the corresponding event types.

Note:
- The broker URL is determined based on the `KAFKA_BOOTSTRAP_SERVER` and `KAFKA_PORT` configuration values.
- The `DEFAULT_TOPIC` and `CONSUMER_CONCURRENCY` configuration values are used to configure the topic and agent
    concurrency.

"""

import faust
from ferrisapp.app import app as ferris_app
from ferrisapp.app import appbuilder

broker = (
    f"kafka://{ferris_app.config.get('KAFKA_BOOTSTRAP_SERVER', 'ferris-broker')}:"
    f"{ferris_app.config.get('KAFKA_PORT', '29092')}"
)

app = faust.App(ferris_app.config["APP_NAME"], broker=broker)


class Event(faust.Record):
    """
    Represents an event record.

    Attributes:
        specversion (str): The spec version of the event.
        id (str): The ID of the event.
        source (str): The source of the event.
        type (str): The type of the event.
        datacontenttype (str): The data content type of the event.
        time (str): The time of the event.
        data (str): The data of the event.
        extensions (dict): Optional extensions for the event. Defaults to an empty dictionary.
        subject (str): The subject of the event. Defaults to None.

    """

    specversion: str
    id: str
    source: str
    type: str
    datacontenttype: str
    time: str
    data: str
    extensions: dict = {}
    subject: str = None


events_topic = app.topic(ferris_app.config.get("DEFAULT_TOPIC", "ferris.events"), value_type=Event)


@app.agent(events_topic, concurrency=ferris_app.config.get("CONSUMER_CONCURRENCY", 1))
async def process(events):
    """
    Async agent that processes events received from the topic.

    It iterates over registered event handlers and triggers them for the corresponding event types.

    Args:
        events: A stream of events received from the topic.

    """
    async for event in events:
        print(event)

        triggerd_handlers = []
        for registered_handler in appbuilder.registered_event_handlers.get(event.type, []):
            registered_handler().process(event)
            triggerd_handlers.append(registered_handler)

        for registered_handler in appbuilder.registered_event_handlers.get("all", []):
            if registered_handler not in triggerd_handlers:
                registered_handler().process(event)
