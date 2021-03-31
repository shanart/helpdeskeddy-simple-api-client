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
    print(classified_name)
    if isinstance(module, ModuleType) and classified_name in module.__dict__:
        RESOURCE_CLASSES[name] = module.__dict__[classified_name]


class Client(object):
    """
    General client class that hold application resources
    """
    def __init__(self, settings=None):
        if settings is not None:
            if 'API_KEY' not in settings.keys():
                raise ValueError('Settings should has "API_KEY" key')
            
            if 'API_ROOT' not in settings.keys():
                raise ValueError('Settings should has "API_ROOT" key')

        self.api_key = base64.b64encode(settings['API_KEY'].encode('ascii')).decode("utf-8")
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
        # TODO: handle files
        """
        # ================ WORKING EXAMPLE ================
        # requests_toolbelt may be very usefull. RTFM - https://toolbelt.readthedocs.io/en/latest/
        from requests_toolbelt import MultipartEncoder
        import magic # is it okay to install whole lib to use only 1 function?

        def get_mime_type(file):
            # Get MIME by reading the header of the file
            initial_pos = file.tell()
            file.seek(0)
            # is it okay to install whole lib ( python-magic ) to use only 1 function?
            mime_type = magic.from_buffer(file.read(1024), mime=True)
            file.seek(initial_pos)
            return mime_type

        postdata = {}
        idx = 0
        # read request data
        for k in fields.keys():
            if 'files' in k:
                # if key starts with "files"
                content_type = get_mime_type(fields[k])
                file = fields[k]

                # save it like a file
                postdata[f'files[{idx}]'] = (
                    file.name, # file name
                    file.file, # file object
                    content_type
                )
                idx += 1
            else:
                postdata[k] = str(fields[k])

        # prepeare proper formatted data
        m = MultipartEncoder(postdata)
        # send reqeust
        r = requests.post(self.url(f'/api/v2/tickets'), 
                            data=m,
                            headers={'Authorization': f'Basic {self.api_key}',
                                     'Content-Type': m.content_type })
        """
        return requests.post(self.url(url), data=data, headers=self.headers())

    def to_url_params(self, params):
        return urllib.parse.urlencode(params)
