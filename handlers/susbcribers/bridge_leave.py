from interfaces.observer import Observer


class BridgeLeave(Observer):
    def handle(self, message):
        print(f"***BridgeLeave, event: {message}")
