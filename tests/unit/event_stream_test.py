from random import randint
from unittest.mock import MagicMock
from uuid import uuid4

import pytest

from eventipy.event import Event
from eventipy.event_stream import EventStream

events: EventStream
event: Event


@pytest.fixture(autouse=True)
def run_around_tests():
    global events, event
    events = EventStream()
    event = Event(str(uuid4()))
    yield


def test_write():
    events.write(event)
    assert events[0] == event


def test_write_integer():
    with pytest.raises(TypeError):
        events.write(0)


def test_set_item():
    events.write(event)
    with pytest.raises(TypeError):
        events[0] = event


def test_get_all_events_by_topic():
    amount_of_events = randint(0, 30)
    topic = str(uuid4())

    for _ in range(amount_of_events):
        events.write(Event(topic))

    topic_events = events.get_by_topic(topic=topic)

    assert len(topic_events) == amount_of_events
    assert len([topic_event for topic_event in topic_events if topic_event.topic == topic]) == len(topic_events)


def test_get_five_events_by_topic():
    amount_of_events = randint(0, 30)
    max_events = randint(0, amount_of_events - 1)
    topic = str(uuid4())

    for _ in range(amount_of_events):
        events.write(Event(topic))

    topic_events = events.get_by_topic(topic=topic, max_events=max_events)

    assert len(topic_events) == max_events
    assert len([topic_event for topic_event in topic_events if topic_event.topic == topic]) == len(topic_events)


def test_get_by_id():
    events.write(event)
    assert events.get_by_id(event.id) == event


def test_subscribe():
    topic = str(uuid4())

    @events.subscribe(topic)
    def handler(event: Event):
        return event.id

    assert handler(event) == event.id
    assert isinstance(events.subscribers[topic], list)


def test_subscribe_event_published():
    @events.subscribe(event.topic)
    def handler(event: Event):
        return event.id

    events.subscribers[event.topic][0] = MagicMock()
    events.write(event)
    events.subscribers[event.topic][0].assert_called_with(event)


def test_add_subscriber():
    events._add_subscriber(event.topic, lambda x: x)
    assert len(events.subscribers[event.topic]) == 1
    events._add_subscriber(event.topic, lambda x: x)
    assert len(events.subscribers[event.topic]) == 2
