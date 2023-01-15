from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def handle(self, message):
        pass
