import json
from interfaces.observer import Observer
from interfaces.subject import Subject
from typing import List


class Plublisher(Subject):
    def __init__(self, events: List[str]):
        self.subscribers = {event: {}
                            for event in events}

    def register(self, event: str, handler: Observer, callback=None):
        if callback is None:
            callback = getattr(handler, "handle")
        self.get_subscribers(event)[handler] = callback

    def dispatch(self, event: str, message: str):
        for subscriber, callback in self.get_subscribers(event).items():
            json_message = json.loads(message.replace("'", "\""))
            callback(json_message)

    def get_subscribers(self, event: str):
        return self.subscribers[event]
