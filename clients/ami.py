import json
from interfaces.client import IClient
from interfaces.subject import Subject
from asterisk.ami import AMIClient, AutoReconnect
# from config.ami import login, connection
from typing import List, Dict
import logging


class Ami(IClient):
    def __init__(self, publisher: Subject, events: List[str], config: Dict):
        self.config = config
        self.client = None
        self.auto_reconnect = None
        self.publisher = publisher
        self.events = events

    def start(self):
        """Start connection and adding listener"""
        self._connect()
        self.client.add_event_listener(
            self.handle_event, white_list=self.events)

    def stop(self):
        """Disconnect from Asterisk Manager Interface"""
        self._disconnect()
        logging.info("Stoping client")

    def _connect(self):
        self.client = AMIClient(**self.config.get("connection"))
        AutoReconnect(self.client)
        future = self.client.login(**self.config.get("login"))

        if future.response.is_error():
            raise Exception(str(future.response))

    def _disconnect(self):
        self.client.logoff()

    def handle_event(self, source, event):
        json_event = json.loads(str(event).split("-> ")[1].replace("'", '"'))
        event_name = str(event).split("-> ")[0].split(': ')[1].strip()
        self.publisher.dispatch(event_name, str(json_event))
