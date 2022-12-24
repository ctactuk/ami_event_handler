from interfaces.observer import Observer


class DialBegin(Observer):
    def handle(self, message):
        print(f"***DialBegin, event: {message}")
