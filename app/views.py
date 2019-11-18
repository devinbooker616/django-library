from django.shortcuts import render, redirect
from django.contrib import messages
from app.models import Book, Transaction
from datetime import datetime

def home(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books} )

def borrow_book(request, id):
    book = Book.objects.get(id=id)
    if book.in_stock:
        messages.success(request, f"Borrowed {book.title} by {book.author}")
        Checkout = book.transaction_set.create(datetime=datetime.now(), action="CHECKOUT", book=book)
        book.in_stock = False
        Checkout.save()
        book.save()
        return redirect("home")
    else:
        messages.error(request, f"{book.title} by {book.author} is unavailable")
        return redirect("home")

def return_book(request, id):           
    book = Book.objects.get(id=id)
    if book.in_stock == False:
        messages.success(request, f"Returned {book.title} by {book.author}")
        Checkin = book.transaction_set.create(datetime=datetime.now(), action="CHECKIN", book=book)
        book.in_stock = True
        Checkin.save()
        book.save()
        return redirect("home")
    else:
        messages.error(request, f"{book.title} by {book.author} is already here")
        return redirect("home")

