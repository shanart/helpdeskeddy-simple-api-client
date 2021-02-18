import requests
from .helpdesk import HelpDeskConnect


class CommentsCRUD(HelpDeskConnect):
    def comments_get(self, ticket_id: int, page: int = 0):
        """
        Get comment by ID
        https://helpdeskeddy.ru/api.html#работа-с-заявками-комментарии-get
        :param ticket_id:
        :param page:
        :return: comments in json format
        """
        r = requests.get(self.url(f'/api/v2/tickets/{ticket_id}/comments/?page={page}'), headers=self.headers())
        return r.json()

    def comment_create(self, ticket_id: int, fields: dict) -> dict:
        """
        Create comment
        https://helpdeskeddy.ru/api.html#работа-с-заявками-комментарии-post
        :param fields: dictionary with post required and non required fields
        :param ticket_id:
        :return: comment
        """
        r = requests.post(self.url(f'/api/v2/tickets/{ticket_id}/comments/'),
                          json=fields,
                          headers=self.headers())
        return r.json()

    def comment_put(self, ticket_id: int, comment_id: int, fields: dict) -> dict:
        """
        Update comment by ID
        https://helpdeskeddy.ru/api.html#работа-с-заявками-комментарии-put
        :param ticket_id:
        :param comment_id:
        :param fields: fields to update
        :return: comment in json format
        """
        r = requests.put(self.url(f'/api/v2/tickets/{ticket_id}/comments/{comment_id}'), json=fields, headers=self.headers())
        return r.json()

    def comment_delete(self, ticket_id: int, comment_id: int) -> dict:
        """
        Remove comment by id
        https://helpdeskeddy.ru/api.html#работа-с-заявками-комментарии-delete
        :param comment_id:
        :param ticket_id:
        :return: success message in dict
        """
        r = requests.delete(self.url(f'/api/v2/tickets/{ticket_id}/comments/{comment_id}/'), headers=self.headers())
        return r.json()
