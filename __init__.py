from .tickets import TicketCRUD
from .posts import PostsCRUD
from .comments import CommentsCRUD

ticket_client = TicketCRUD()
posts_client = PostsCRUD()
comments_client = CommentsCRUD()
