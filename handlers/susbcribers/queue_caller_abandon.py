from interfaces.observer import Observer


class QueueCallerAbandon(Observer):
    def handle(self, message):
        print(f"***QueueCallerAbandon, event: {message}")
