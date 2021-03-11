from .base import Essence


class Ticket(Essence):
    # TODO: describe all required methods

    def change_status(self, id):
        """Change ticket status by status id
        NOTE: Need to actualize some how status id's to prevent 
        something like: Status not fined by given id """
        pass

    def freeze_date(self, date):
        """Freeze ticket due to given date and time"""
        pass