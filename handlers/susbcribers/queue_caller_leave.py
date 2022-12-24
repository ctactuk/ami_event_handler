from interfaces.observer import Observer


class QueueCallerLeave(Observer):
    def handle(self, message):
        print(f"***QueueCallerLeave, event: {message}")
