"""

NOTE: Usage example

from helpdesckeddy import Client

client = Client(config)

client.tickets.get(id)
client.tickets.update(dict)
client.tickets.delete(id)
client.tickets.create(dict)

client.messages.get(ticket_id)
client.messages.create(ticket_id, dict)
client.messages.update(ticket_id, dict)

"""

from types import ModuleType
from pprint import pprint
import base64
import json
import urllib
import requests
import string

from . import resources


# Save all modules from resources package in dict
RESOURCE_CLASSES = {}
for name, module in resources.__dict__.items():
    classified_name = string.capwords(name, '_').replace('_', '')
    if isinstance(module, ModuleType) and classified_name in module.__dict__:
        RESOURCE_CLASSES[name] = module.__dict__[classified_name]


class Client(object):

    def __init__(self, settings=None):
        if settings is not None:
            if 'API_KEY' not in settings.keys():
                raise ValueError('Settings should has "API_KEY" key')
            
            if 'API_ROOT' not in settings.keys():
                raise ValueError('Settings should has "API_ROOT" key')

        self.api_key = base64.b64encode(settings['API_KEY'].encode('ascii')).decode("utf-8")
        self.api_root = settings['API_ROOT']

        for name, Klass in RESOURCE_CLASSES.items():
            setattr(self, name, Klass(self))

    def headers(self) -> dict:
        """
        Create authorization headers:
        Docs: https://helpdeskeddy.ru/api.html#обзор
        """
        
        return {
            'Authorization': f'Basic {self.api_key}',
            'Cache-Control': 'no-cache'      
            # TODO: What content-type should be in multipart/form-data requests?
            # 'Content-Type': 'application/json'
        }

    def url(self, url: str) -> str:
        """
        API calls url formatter
        """
        return f'{self.api_root}{url}'