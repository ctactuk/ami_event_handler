from abc import ABC, abstractmethod
from interfaces.observer import Observer


class Subject(ABC):
    @abstractmethod
    def register(self, event: str, handler: Observer, callback: str = None):
        pass

    @abstractmethod
    def unregister(self, event: str, handler: Observer):
        pass

    @abstractmethod
    def dispatch(self, event, message):
        pass
    
    @abstractmethod
    def get_subscribers(self, event: str):
        pass
