from interfaces.observer import Observer


class Reload(Observer):
    def handle(self, message):
        print(f"***Reload, event: {message}")
