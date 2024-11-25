from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from core.models import Book, Genre
from core.forms import BookForm
from django.db.models import QuerySet
from typing import Union


def paginate_queryset(request: HttpRequest, queryset: QuerySet, per_page: int = 6) -> Paginator.page:
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def home_view(request: HttpRequest) -> HttpResponse:
    books = Book.objects.prefetch_related('genres').all()
    page_obj = paginate_queryset(request, books)
    return render(request, 'home.html', {'page_obj': page_obj})


def catalog_view(request: HttpRequest) -> HttpResponse:
    genres = Genre.objects.all()
    return render(request, 'catalog.html', {'genres': genres})


def genre_books_view(request: HttpRequest, genre_id: int) -> HttpResponse:
    genre = get_object_or_404(Genre, id=genre_id)
    books = genre.books.all()
    return render(request, 'genre_books.html', {'genre': genre, 'books': books})


def book_detail_view(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_object_or_404(Book.objects.prefetch_related('genres'), id=book_id)
    is_owner = request.user.is_authenticated and book.added_by == request.user
    return render(request, 'book_detail.html', {'book': book, 'is_owner': is_owner})


@login_required
def add_book_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user
            book.save()
            form.save_m2m()
            return redirect('profile')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


@login_required
def user_books_view(request: HttpRequest) -> HttpResponse:
    books = Book.objects.filter(added_by=request.user)
    return render(request, 'user_books.html', {'books': books})


@login_required
def edit_book_view(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_object_or_404(Book, id=book_id, added_by=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('user_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})


@login_required
def delete_book_view(request: HttpRequest, book_id: int) -> Union[HttpResponse, None]:
    book = get_object_or_404(Book, id=book_id, added_by=request.user)
    if request.method == 'GET':
        book.delete()
        return redirect('user_books')
    return render(request, 'delete_book.html', {'book': book})
