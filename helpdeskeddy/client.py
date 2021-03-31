import os
import base64
import json
import urllib
import requests
import string
import magic  # is it okay to install whole lib to use only 1 function Client.get_mime_type() ?

from types import ModuleType

# requests_toolbelt may be very usefull. RTFM - https://toolbelt.readthedocs.io/en/latest/
from requests_toolbelt import MultipartEncoder
from . import resources


# Save all modules from resources package in dict
RESOURCE_CLASSES = {}
for name, module in resources.__dict__.items():
    classified_name = string.capwords(name, '_').replace('_', '')
    if isinstance(module, ModuleType) and classified_name in module.__dict__:
        RESOURCE_CLASSES[name] = module.__dict__[classified_name]


class Client(object):
    tickets = None
    """
    General client class that hold application resources
    """

    def __init__(self, settings=None):
        if settings is not None:
            if 'API_KEY' not in settings.keys():
                raise ValueError('Settings should has "API_KEY" key')

            if 'API_ROOT' not in settings.keys():
                raise ValueError('Settings should has "API_ROOT" key')

        self.api_key = base64.b64encode(
            settings['API_KEY'].encode('ascii')).decode("utf-8")
        self.api_root = settings['API_ROOT'] + '/api/v2'

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
        }

    def url(self, url: str) -> str:
        """
        API calls url formatter
        """
        return f'{self.api_root}{url}'

    def get(self, query):
        return requests.get(self.url(query), headers=self.headers())

    def post(self, url, data):
        encoded_data = MultipartEncoder(data)
        return requests.post(self.url(url),
                        data=encoded_data,
                        headers={'Authorization': f'Basic {self.api_key}',
                                'Content-Type': encoded_data.content_type})

    def to_url_params(self, params):
        return urllib.parse.urlencode(params)

    def get_mime_type(self, file):
        mime_type = magic.from_file(file, mime=True)
        return mime_type

    def get_file_name(self, path):
        return os.path.basename(path)