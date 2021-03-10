import requests
from helpdesk import HelpDeskConnect
from schema.tickets import GetTicketsUrlParamsSchema


class TicketCRUD(HelpDeskConnect):
    """
    Class describe CRUD interactions with the system
    
    ...
    Methods
    -------
    ticket_all()
        Get all
    ticket_post
        create new one
    ticket_get
        get by
    ticket_put
        update 
    ticket_delete
        delete
    """

    def ticket_all(self, url_arg: str) -> dict:
        """
        Example testing request
        https://helpdeskeddy.ru/api.html#работа-с-заявками-заявки
        """
        r = requests.get(self.url(f'/api/v2/tickets/{url_arg}'), headers=self.headers())
        return r.json()

    def ticket_post(self, fields: dict):
        """
        Create Ticket
        :param fields: dictionary with ticket required and non required fields
        :return: Ticket
        """
        r = requests.post(self.url(f'/api/v2/tickets'),
                          json=fields,
                          headers=self.headers())
        return r.json()['data']

    def ticket_get(self, ticket_id: int) -> id:
        """
        Get ticket by ID
        :param ticket_id:
        :return: ticket in json format
        """
        r = requests.get(self.url(f'/api/v2/tickets/{ticket_id}'), headers=self.headers())
        return r.json()

    def ticket_put(self, ticket_id: int, fields: dict) -> dict:
        """
        Update ticket by ID
        :param ticket_id:
        :param fields: fields to update
        :return: ticket in json format
        """
        r = requests.put(self.url(f'/api/v2/tickets/{ticket_id}'), json=fields, headers=self.headers())
        return r.json()

    def ticket_delete(self, ticket_id: int):
        """
        Remove ticket by id
        :param ticket_id:
        :return:
        """
        r = requests.delete(self.url(f'/api/v2/tickets/{ticket_id}'), headers=self.headers())
        return r.json()
