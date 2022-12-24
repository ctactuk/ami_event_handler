import os

connection = {
    'address': os.environ.get('ARI_HOST_ADDRESS'),
    'port': int(os.environ.get('ARI_PORT')),
    'timeout': int(os.environ.get('ARI_TIMEOUT')),
}

login = {
    'username': os.environ.get('ARI_USERNAME'),
    'secret': os.environ.get('ARI_SECRET')
}
