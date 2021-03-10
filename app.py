import os
from dotenv import load_dotenv
from pathlib import Path
import requests
from helpdeskeddy import *

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, '.env'))

HELPDESK_API_ROOT = os.getenv('HELPDESK_API_ROOT')
HELPDESK_API_KEY = os.getenv('HELPDESK_API_KEY')
