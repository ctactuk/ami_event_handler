from interfaces.observer import Observer


class BridgeDestroy(Observer):
    def handle(self, message):
        print(f"***BridgeDestroy, event: {message}")
