from django.shortcuts import render, redirect
from .models import Book, Reservation
from .forms import ReservationForm

def booking_render(request):
    book = Book.objects.all().order_by('-updated_on').first()
    form = None
    success = False
    reservations = None

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReservationForm(request.POST)
            if form.is_valid():
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.save()
                success = True
        else:
            form = ReservationForm()

        # Only fetch reservations if user is logged in
        reservations = Reservation.objects.filter(user=request.user).order_by('-created_date')

    return render(request, "book/book.html", {
        "book": book,
        "form": form,
        "success": success,
        "reservations": reservations,
    })