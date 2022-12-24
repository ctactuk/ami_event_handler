from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def handle(message):
        pass
