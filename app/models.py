from django.db import models
from datetime import datetime

class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    published = models.DateField(datetime.now())
    genre = models.TextField()
    in_stock = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Transaction(models.Model):
    datetime = models.DateField(datetime.now())
    action = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.PROTECT)