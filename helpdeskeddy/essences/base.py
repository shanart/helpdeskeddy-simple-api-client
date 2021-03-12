from abc import ABC, abstractmethod


class Essence(ABC):

    # https://pymotw.com/3/abc/
    # __metaclass__ = abc.ABCMeta


    @abstractmethod
    def get(self, url):
        """GET method.

        Args:
            url (str): URL string

        Returns:
            HTTP response
        """
        pass

    @abstractmethod
    def create(self, payload: dict):
        """POST method.

        Args:
            payload (dict): method payload dict contain required fields

        Returns:
            HTTP response
        """
        pass

    @abstractmethod
    def update(self, payload: dict):
        """UPDATE method. Describe HTTP PUT method.

        Args:
            payload (int): method payload dict contain fields that needs to be updated

        Returns:
            HTTP response
        """
        pass

    @abstractmethod
    def delete(self, id):
        """DELETE method.

        Args:
            id (int): unique identifier of entity needs to be deleted

        Returns:
            HTTP 204, no-content
        """
        pass