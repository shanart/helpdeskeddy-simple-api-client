from pprint import pprint
import os
from dotenv import load_dotenv
from pathlib import Path
import requests

from helpdeskeddy import Client 

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(os.path.join(BASE_DIR, '.env'))

HELPDESK_API_ROOT = os.getenv('HELPDESK_API_ROOT')
HELPDESK_API_KEY = os.getenv('HELPDESK_API_KEY')


config = {
    'API_KEY': HELPDESK_API_KEY,
    'API_ROOT': HELPDESK_API_ROOT
}

client = Client(config)

pprint(client.tickets.__dict__)
pprint(client.comments.__dict__)
