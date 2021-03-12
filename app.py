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


settings = {
    'API_KEY': HELPDESK_API_KEY,
    'API_ROOT': HELPDESK_API_ROOT
}


client = Client(settings)
pprint(client.get_ticket('order_by=viewed_by_staff{ASC}'), indent=4)

