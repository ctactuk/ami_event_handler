import os
config = {
    "connection" : {
        'address': os.environ.get('AMI_HOST_ADDRESS'),
        'port': int(os.environ.get('AMI_PORT')),
        'timeout': int(os.environ.get('AMI_TIMEOUT')),
    },
    "login" : {
        'username': os.environ.get('AMI_USERNAME'),
        'secret': os.environ.get('AMI_SECRET')
    }
}