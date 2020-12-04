from collections.abc import Sequence
from typing import List
from uuid import UUID

from eventipy.event import Event


class EventStream(Sequence):
    def __init__(self):
        self.__events: List[Event] = []

    def write(self, event: Event):
        if not isinstance(event, Event):
            raise TypeError("event must be of type Event")

        if self.get_by_id(event.id):
            raise ValueError(f"event with {event.id} already written")

        self.__events.append(event)

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
