from types import FunctionType
import base64
import json
import urllib

from .essences import Tickets


class Client(Tickets):
    def __init__(self, settings):

        if 'API_KEY' not in settings:
            raise ValueError('Settings should has "API_KEY" key')
        
        if 'API_ROOT' not in settings:
            raise ValueError('Settings should has "API_ROOT" key')
            
        self.api_key = base64.b64encode(settings['API_KEY'].encode('ascii')).decode("utf-8")
        self.api_root = settings['API_ROOT']


    def headers(self) -> dict:
        """
        Create authorization headers:
        Docs: https://helpdeskeddy.ru/api.html#обзор
        """
        return {
            'Authorization': f'Basic {self.api_key}',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/json'
        }

    def url(self, url: str) -> str:
        """
        API calls url formatter
        """
        return f'{self.api_root}{url}'

    # @validate_<essence name>(url_params)
    # def get_<essence name>(self, url_params)

    # @validate_<essence name>(payload)
    # def create_<essence name>(self, payload: dict):

    # @validate_<essence name>(payload)
    # def update_<essence name>(self, payload: dict):

    # def delete_<essence name>(self, id):
