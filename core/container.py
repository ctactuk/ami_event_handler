from dependency_injector import containers, providers

events = ['PeerStatus', 'QueueCallerAbandon', 'QueueCallerJoin', 'QueueCallerLeave',
          'Reload', 'BridgeCreate', 'BridgeDestroy', 'BridgeEnter', 'BridgeLeave', 'DialBegin',
          'DialEnd']

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    # ami_client = providers.Singleton(AMIClient, **connection)
    # asterisk_client = providers.Singleton()