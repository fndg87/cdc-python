from pact import Term


class ConsumerConfig(object):

    authenticate = {
        'path': '/api/v1/auth/authenticate/',
        'request_headers': {'Content-Type': 'application/json'},
        'request_payload': {
            "username": "your_admin_user",
            "password": "your_password"
        },
        # this will validate the response has the UUID format (if the default value is not met)
        'response_body_matcher': {
            "token": Term('[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}', 'edff372c-55de-11e7-907b-a6006ad3dba0')
        }
    }

    def __init__(self):
        pass


