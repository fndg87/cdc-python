import atexit
import json
import unittest

from pact import Consumer, Provider

from client.authenthicate import AuthenticateRequest
from configurations.consumer_configurations import ConsumerConfig

pact = Consumer('consumer_app').has_pact_with(Provider('provider_api'), host_name='localhost', port=9191,
                                              pact_dir='./consumer_app_and_api_contracts')
pact.start_service()
atexit.register(pact.stop_service)


class UserContract(unittest.TestCase):
    def test_admin_user_authentication(self):
        (pact
         .given('An administrator user')
         .upon_receiving('an authentication request')
         .with_request('post', ConsumerConfig.authenticate['path'])
         .will_respond_with(status=200, body=ConsumerConfig.authenticate['response_body_matcher'])
         )

        with pact:
            request = AuthenticateRequest()
            result = request.authenticate_request("http://localhost:9191")

        self.assertEqual(result.json(), json.loads('{"token":"edff372c-55de-11e7-907b-a6006ad3dba0"}'))
