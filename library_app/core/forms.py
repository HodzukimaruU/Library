from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Genre

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=15, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''


class BookForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        label="Заголовок",
        widget=forms.TextInput(attrs={'placeholder': 'Введите название книги'}),
    )
    author = forms.CharField(
        max_length=100,
        label="Автор",
        widget=forms.TextInput(attrs={'placeholder': 'Введите автора книги'}),
    )
    cover_image = forms.ImageField(
        label="Обложка книги",
    )
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        label="Жанры"
    )
    publication_date = forms.DateField(
        label="Дата публикации",
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
    pages = forms.CharField(
        max_length=100,
        label="Страницы",
        widget=forms.TextInput(attrs={'placeholder': 'Введите количество страниц книги'}),
    )
    description = forms.CharField(
        required=False,
        label="Описание книги",
        widget=forms.Textarea(attrs={'placeholder': 'Введите описание книги', 'class': 'no-resize'}),
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'cover_image', 'genres', 'publication_date', 'pages', 'description']
