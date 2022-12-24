from dependency_injector import containers, providers
from asterisk.ami import AMIClient, AutoReconnect
from config.ami import login, connection


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    ami_client = providers.Singleton(AMIClient, **connection)
    asterisk_client = providers.Singleton()