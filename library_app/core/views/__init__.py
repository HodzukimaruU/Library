from .confirm_email import confirm_email_view, confirm_email_stub_controller
from .register import register_view
from .login import login_view, logout_view
from .profile import profile_view
from .catalog_and_book import home_view, catalog_view, genre_books_view, book_detail_view, edit_book_view, delete_book_view, add_book_view, user_books_view


__all__ = ["confirm_email_view", "confirm_email_stub_controller", "register_view", "login_view", 
           "logout_view", "profile_view", "home_view", "catalog_view", "genre_books_view", "book_detail_view", "add_book_view",
           "edit_book_view", "delete_book_view", "user_books_view"]
