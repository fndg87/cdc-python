import requests

from configurations.consumer_configurations import ConsumerConfig


class AuthenticateRequest(object):
    @staticmethod
    def authenticate_request( url):
        r = requests.post(url + ConsumerConfig.authenticate['path'],
                          headers=ConsumerConfig.authenticate['request_headers'],
                          json=ConsumerConfig.authenticate['request_payload']
                          )
        return r
