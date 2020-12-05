from uuid import uuid4


class Event:
    def __init__(self, topic: str):
        self.id = uuid4()
        self.topic = topic
