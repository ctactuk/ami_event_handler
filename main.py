from handlers.events.publisher import Plublisher
from handlers.susbcribers.peer_status import PeerStatus
from handlers.susbcribers.queue_caller_abandon import QueueCallerAbandon
from handlers.susbcribers.queue_caller_join import QueueCallerJoin
from handlers.susbcribers.reload import Reload
from handlers.susbcribers.bridgeenter import BridgeEnter
from handlers.susbcribers.queue_caller_leave import QueueCallerLeave
from handlers.susbcribers.bridge_create import BridgeCreate
from handlers.susbcribers.bridge_destroy import BridgeDestroy
from handlers.susbcribers.bridge_leave import BridgeLeave
from handlers.susbcribers.dial_begin import DialBegin
from handlers.susbcribers.dial_end import DialEnd
from clients.ami import Ami
from config.ami import config as ami_config
import time

from core.container import Container

events = ['PeerStatus', 'QueueCallerAbandon', 'QueueCallerJoin', 'QueueCallerLeave',
          'Reload', 'BridgeCreate', 'BridgeDestroy', 'BridgeEnter', 'BridgeLeave', 'DialBegin',
          'DialEnd']

publisher = Plublisher(events)

publisher.register("PeerStatus", PeerStatus())
publisher.register("QueueCallerAbandon", QueueCallerAbandon())
publisher.register("QueueCallerJoin", QueueCallerJoin())
publisher.register("Reload", Reload())
publisher.register("BridgeEnter", BridgeEnter())
publisher.register("QueueCallerLeave", QueueCallerLeave())
publisher.register("BridgeCreate", BridgeCreate())
publisher.register("BridgeDestroy", BridgeDestroy())
publisher.register("BridgeLeave", BridgeLeave())
publisher.register("DialBegin", DialBegin())
publisher.register("DialEnd", DialEnd())


ami_client = Ami(publisher, events, ami_config)


def main():
    try:
        ami_client.start()
        while True:
            time.sleep(10)
    except (KeyboardInterrupt, SystemExit, Exception):
        ami_client.stop()


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])
    main()
