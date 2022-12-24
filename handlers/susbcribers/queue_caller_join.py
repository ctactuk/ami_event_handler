from interfaces.observer import Observer


class QueueCallerJoin(Observer):
    def handle(self, message):
        print(f"***QueueCallerJoin, event: {message}")
