from interfaces.observer import Observer

class DialEnd(Observer):
    def handle(self, message):
        print(f"***DialEnd, event: {message}")