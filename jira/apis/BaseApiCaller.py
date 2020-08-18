import json
import logging

import requests

logger = logging.getLogger(__name__)


class BaseApiCaller:
    url = None
    access_token = None
    client_id = None
    client_secret = None

    def __init__(self, environment_variables):
        self.url = environment_variables['url']

        self.client_id = \
            environment_variables['clientId']

        self.client_secret = \
            environment_variables['clientSecret']

    def get_session(self):
        auth = (self.client_id, self.client_secret)
        return auth

    def get(self, api):
        auth = self.get_session()

        formatted_api_url = self.url + api

        formatted_api_response = requests.get(formatted_api_url, auth=auth)

        logger.info(api + ' : STATUS CODE : {}'.format(formatted_api_response.status_code))
        if formatted_api_response.status_code == 200:
            response = formatted_api_response.text
            return json.loads(response)
        else:
            return

    def post(self, api, payload):
        auth = self.get_session()
        formatted_api_url = self.url + api

        formatted_api_response = requests.post(formatted_api_url, auth=auth, json=payload)
        logger.info(api + ' : STATUS CODE : {}'.format(formatted_api_response.status_code))

        if formatted_api_response.status_code == 200 or formatted_api_response.status_code == 201:
            response = formatted_api_response.text
            return json.loads(response)
        else:
            return
