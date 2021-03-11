"""

NOTE: This file is DEPRECATED. Entry point moved to client.py

"""
import base64
import requests
import json
import urllib


class HelpDeskConnect:
    def __init__(self, key='', api_root=''):
        """
        Initializing with default key from app settings file
        """
        self.api_key = base64.b64encode(key.encode('ascii')).decode("utf-8")
        self.api_root = api_root

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

    def get_departments(self) -> dict:
        """
        Example testing request
        """
        r = requests.get(self.url('/api/v2/departments/'), headers=self.headers())
        return r.json()
