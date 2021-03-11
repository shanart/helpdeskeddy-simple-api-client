import base64
import requests
import json
import urllib


class Client:
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
    
    
    # HTTP methods
    def get(self, url) -> dict:
        """
        Basic GET request.
        """
        r = requests.get(self.url(url), headers=self.headers())
        return r.json()