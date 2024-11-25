from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


import uuid
import time


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ConfirmationCode(BaseModel):
    code = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="confirmations")
    expiration_time = models.IntegerField()

    def is_expired(self):
        return time.time() > self.expiration_time


class Genre(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(BaseModel):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    pages = models.PositiveIntegerField()
    description = models.TextField()
    cover_image = models.ImageField(upload_to='photo/', blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name='books')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='added_books', null=True)

    def __str__(self):
        return self.title
