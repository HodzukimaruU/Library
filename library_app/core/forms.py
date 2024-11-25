from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Genre

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=15, required=True)
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
        label="Title",
        widget=forms.TextInput(attrs={'placeholder': 'Enter the book title'}),
    )
    author = forms.CharField(
        max_length=100,
        label="Author",
        widget=forms.TextInput(attrs={'placeholder': 'Enter the author of the book'}),
    )
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        label="Genres"
    )
    publication_date = forms.DateField(
        label="Publication date",
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
    pages = forms.CharField(
        max_length=100,
        label="Pages",
        widget=forms.TextInput(attrs={'placeholder': 'Enter the number of book pages'}),
    )
    description = forms.CharField(
        required=False,
        label="Description of the book",
        widget=forms.Textarea(attrs={'placeholder': 'Enter book description', 'class': 'no-resize'}),
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'cover_image', 'genres', 'publication_date', 'pages', 'description']
