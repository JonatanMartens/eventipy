from uuid import uuid4


class Event(object):
    def __init__(self, topic: str):
        self.id = uuid4()
        self.topic = topic
