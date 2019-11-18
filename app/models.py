from django.db import models
from datetime import datetime


class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    published = models.DateField()
    genre = models.TextField()
    in_stock = models.BooleanField()
    description = models.TextField()


class Transaction(models.Model):
    datetime = models.DateTimeField()
    action = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
