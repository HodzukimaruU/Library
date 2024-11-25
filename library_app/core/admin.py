from django.contrib import admin
from .models import Genre, Book


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publication_date', 'pages', 'description')
    search_fields = ('title', 'author')
    list_filter = ('publication_date', 'genres')
    filter_horizontal = ('genres',)
    date_hierarchy = 'publication_date'
