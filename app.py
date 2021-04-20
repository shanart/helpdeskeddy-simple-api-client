from pprint import pprint
import os
import json
from dotenv import load_dotenv
from pathlib import Path
import requests

from helpdeskeddy import Client
from helpdeskeddy.client import RESOURCE_CLASSES

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(os.path.join(BASE_DIR, '.env'))

HELPDESK_API_ROOT = os.getenv('HELPDESK_API_ROOT')
HELPDESK_API_KEY = os.getenv('HELPDESK_API_KEY')


config = {
    'API_KEY': HELPDESK_API_KEY,
    'API_ROOT': HELPDESK_API_ROOT
}

client = Client(config)

attachment = "./media/attachment.jpeg"

ticket_post_data = {
    "title": "api test data 15",
}

req = client.tickets.put(83, ticket_post_data)

print(req)
print(req.text)
