from interfaces.observer import Observer


class PeerStatus(Observer):
    def handle(self, message):
        print(f"***PeerStatus, event: {message}")
