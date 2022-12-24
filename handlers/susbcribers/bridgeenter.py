from interfaces.observer import Observer


class BridgeEnter(Observer):
    def handle(self, message):
        print(f"***BridgeEnter, event: {message}")
