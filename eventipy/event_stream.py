import logging
from collections.abc import Sequence
from functools import wraps
from typing import List, Callable, Dict
from uuid import UUID

from eventipy.event import Event

logger = logging.getLogger(__name__)


class EventStream(Sequence):
    def __init__(self):
        self.__events: List[Event] = []
        self.subscribers: Dict[str, List[Callable]] = {}

    def write(self, event: Event):
        if not isinstance(event, Event):
            raise TypeError("event must be of type Event")

        if self.get_by_id(event.id):
            raise ValueError(f"event with {event.id} already written")

        self.__events.append(event)
        self._publish_to_subscribers(event)

    def _publish_to_subscribers(self, event: Event):
        try:
            for handler in self.subscribers[event.topic]:
                handler(event)
        except KeyError:
            pass

    def subscribe(self, topic: str) -> Callable:
        def wrapper(fn: Callable[..., None]):
            @wraps(fn)
            def handle_event(event: Event):
                try:
                    fn(event)
                except Exception as e:
                    logger.warning(f"{fn.__name__} failed to handle event of topic {topic}. Exception: {e}")

            self._add_subscriber(topic, handler=handle_event)
            return fn

        return wrapper

    def _add_subscriber(self, topic: str, handler: Callable):
        try:
            self.subscribers[topic].append(handler)
        except KeyError:
            self.subscribers[topic] = [handler]

    def get_by_id(self, event_id: UUID) -> Event:
        for event in self.__events:
            if event.id == event_id:
                return event

    def get_by_topic(self, topic: str, max_events: int = None) -> List[Event]:
        matching_events = []
        for event in self.__events:
            if event.topic == topic:
                matching_events.append(event)
            if max_events and len(matching_events) >= max_events:
                break
        return matching_events

    def __len__(self) -> int:
        return len(self.__events)

    def __getitem__(self, i: int) -> Event:
        return self.__events[i]

    def __setitem__(self, key, value):
        raise TypeError("EventStream object does not support item assignment")

    def __repr__(self):
        return repr(self.__events)

    def __str__(self):
        return str(self.__events)


events = EventStream()
