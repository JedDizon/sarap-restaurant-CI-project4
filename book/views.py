from django.shortcuts import get_object_or_404, render, redirect
from .models import Reservation, Book
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

def booking_render(request):
    book = Book.objects.all().order_by('-updated_on').first()
    form = None
    success = False
    edit_id = request.POST.get('edit_id') 
    edit_form = None
    reservations = None

    if request.user.is_authenticated:
        if request.method == 'POST':
            if 'edit_id' in request.POST:
                reservation = get_object_or_404(Reservation, pk=edit_id)

                if reservation.user != request.user and not request.user.is_staff:
                    return render(request, "book/book.html", {
                        "book": book,
                        "error": "You do not have permission to edit this reservation.",
                    })

                if reservation.status == 'declined':
                    return render(request, "book/book.html", {
                        "book": book,
                        "error": "This reservation was declined and cannot be modified.",
                    })

                edit_form = ReservationForm(request.POST, instance=reservation)
                if edit_form.is_valid():
                    updated = edit_form.save(commit=False)
                    if reservation.status == 'approved':
                        updated.status = 'pending'
                    updated.save()
                    success = True
                    edit_id = None
                    edit_form = None
            else:
                form = ReservationForm(request.POST)
                if form.is_valid():
                    reservation = form.save(commit=False)
                    reservation.user = request.user
                    reservation.save()
                    success = True
        else:
            form = ReservationForm()

        reservations = Reservation.objects.filter(user=request.user).order_by('-created_date')

    return render(request, "book/book.html", {
        "book": book,
        "form": form,
        "success": success,
        "reservations": reservations,
        "edit_form": edit_form,
        "edit_id": edit_id,
    })