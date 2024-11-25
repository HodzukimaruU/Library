from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    profile_view,
    register_view,
    login_view, logout_view,
    confirm_email_view, confirm_email_stub_controller,
    home_view, catalog_view, genre_books_view, book_detail_view,
    edit_book_view, delete_book_view, user_books_view, add_book_view   
    )

urlpatterns = [
    path('', home_view, name='home'),
    path('profile/', profile_view, name='profile'),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('confirm-email/', confirm_email_view, name='confirm_email'),
    path('confirm-email-sent/', confirm_email_stub_controller, name='confirm_email_sent'),

    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('catalog/', catalog_view, name='catalog'),
    path('catalog/<int:genre_id>/', genre_books_view, name='genre_books'),
    path('books/', user_books_view, name='user_books'),
    path('book/<int:book_id>/', book_detail_view, name='book_detail'),
    path('books/<int:book_id>/edit/', edit_book_view, name='edit_book'),
    path('books/<int:book_id>/delete/', delete_book_view, name='delete_book'),
    path('add_book/', add_book_view, name='add_book'),
]

