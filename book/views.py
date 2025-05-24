from django.shortcuts import get_object_or_404, render
from .models import Reservation, Book
from .forms import ReservationForm
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
from django.shortcuts import redirect

def booking_render(request):
    book = Book.objects.all().order_by('-updated_on').first()
    form = None
    success = False
    edit_id = request.POST.get('edit_id')
    edit_form = None
    reservations = None

    if request.user.is_authenticated:
        # Auto-delete outdated reservations
        cutoff = timezone.now().date() - timedelta(days=5)

        Reservation.objects.filter(
            status='declined',
            updated_on__lt=timezone.now() - timedelta(days=5)
        ).delete()

        Reservation.objects.filter(
            status='approved',
            requested_date__lt=cutoff
        ).delete()

        if request.method == 'POST':
            # DELETE logic
            if 'delete_id' in request.POST:
                delete_id = request.POST.get('delete_id')
                reservation_to_delete = get_object_or_404(Reservation, pk=delete_id)

                if reservation_to_delete.user != request.user and not request.user.is_staff:
                    return render(request, "book/book.html", {
                        "book": book,
                        "error": "You do not have permission to cancel this reservation.",
                    })

                reservation_to_delete.delete()
                messages.success(request, "Your reservation has been cancelled.")
                return redirect('book') 

            # EDIT logic
            elif 'edit_id' in request.POST:
                reservation_to_edit = get_object_or_404(Reservation, pk=edit_id)

                if reservation_to_edit.user != request.user and not request.user.is_staff:
                    return render(request, "book/book.html", {
                        "book": book,
                        "error": "You do not have permission to edit this reservation.",
                    })

                if reservation_to_edit.status == 'declined':
                    return render(request, "book/book.html", {
                        "book": book,
                        "error": "This reservation was declined and cannot be modified.",
                    })

                edit_form = ReservationForm(request.POST, instance=reservation_to_edit)
                if edit_form.is_valid():
                    updated = edit_form.save(commit=False)
                    if reservation_to_edit.status == 'approved':
                        updated.status = 'pending'
                    updated.save()
                    messages.success(request, "Your reservation has been updated!")
                    return redirect('book') 
                    edit_id = None
                    edit_form = None

            # CREATE logic
            else:
                form = ReservationForm(request.POST)
                if form.is_valid():
                    new_reservation = form.save(commit=False)
                    new_reservation.user = request.user
                    new_reservation.save()
                    messages.success(request, "Your reservation has been submitted!")
                    return redirect('book') 
        else:
            form = ReservationForm()

        reservations = Reservation.objects.filter(user=request.user).order_by('-updated_on')

    return render(request, "book/book.html", {
        "book": book,
        "form": form,
        "success": success,
        "reservations": reservations,
        "edit_form": edit_form,
        "edit_id": edit_id,
    })