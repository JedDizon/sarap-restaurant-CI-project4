from django.shortcuts import render
from .models import Book


def booking_render(request):
    """
    Renders the Book page
    """
    book = Book.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "book/book.html",
        {"book": book},
    )