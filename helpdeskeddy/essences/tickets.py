# from .base import Essence
import requests

class Tickets:

    API_ROOT = "/api/v2/tickets/"

    # # HTTP methods
    def get_ticket(self, url) -> dict:
        query_url = self.url(self.API_ROOT + '?' + url)
        r = requests.get(query_url, headers=self.headers())
        return r.json()

    # def create_ticket(self, payload: dict):
    #     pass

    # def update_ticket(self, payload: dict):
    #     pass

    # def delete_ticket(self, id):
    #     pass

    def change_status(self, id):
        """Change ticket status by status id
        NOTE: Need to actualize some how status id's to prevent 
        something like: Status not fined by given id """
        pass

    def freeze_date(self, date):
        """Freeze ticket due to given date and time"""
        pass