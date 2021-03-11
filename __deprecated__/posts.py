import requests
from .helpdesk import HelpDeskConnect


class PostsCRUD(HelpDeskConnect):
    def posts_get(self, ticket_id: int, page: int = 0):
        """
        Get post by ID
        https://helpdeskeddy.ru/api.html#работа-с-заявками-ответы-в-заявке-get
        :param ticket_id:
        :param page:
        :return: post in json format
        """
        r = requests.get(self.url(f'/api/v2/tickets/{ticket_id}/posts/?page={page}'), headers=self.headers())
        return r.json()

    def post_create(self, ticket_id: int, fields: dict) -> dict:
        """
        Create post
        https://helpdeskeddy.ru/api.html#работа-с-заявками-ответы-в-заявке-post
        :param fields: dictionary with post required and non required fields
        :param ticket_id:
        :return: post
        """
        r = requests.post(self.url(f'/api/v2/tickets/{ticket_id}/posts/'),
                          json=fields,
                          headers=self.headers())
        return r.json()

    def post_put(self, ticket_id: int, post_id: int, fields: dict) -> dict:
        """
        Update post by ID
        https://helpdeskeddy.ru/api.html#работа-с-заявками-ответы-в-заявке-put
        :param ticket_id:
        :param post_id:
        :param fields: fields to update
        :return: post in json format
        """
        r = requests.put(self.url(f'/api/v2/tickets/{ticket_id}/posts/{post_id}'), json=fields, headers=self.headers())
        return r.json()

    def post_delete(self, ticket_id: int, post_id: int):
        """
        Remove post by id
        https://helpdeskeddy.ru/api.html#работа-с-заявками-ответы-в-заявке-delete
        :param post_id:
        :param ticket_id:
        :return:
        """
        r = requests.delete(self.url(f'/api/v2/tickets/{ticket_id}/posts/{post_id}/'), headers=self.headers())
        return r.json()
