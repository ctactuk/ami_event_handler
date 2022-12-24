from interfaces.observer import Observer


class BridgeCreate(Observer):
    def handle(self, message):
        print(f"***BridgeCreate, event: {message}")
