import json

class SqsEventHandler:
    def __init__(self, event):
        self.event = event
        self._queue_messages = None

    @property
    def queue_messages(self):
        if self._queue_messages is None:
            self._queue_messages = self.event.get('Records', [])
        return self._queue_messages