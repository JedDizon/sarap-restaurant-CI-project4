from django import forms
from django.utils import timezone
from datetime import time
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['requested_date', 'requested_time', 'seats', 'guest_name', 'guest_phone']
        widgets = {
            'requested_date': forms.DateInput(attrs={'type': 'date'}),
            'requested_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        requested_date = cleaned_data.get("requested_date")
        requested_time = cleaned_data.get("requested_time")

        if not requested_date or not requested_time:
            return cleaned_data

        now = timezone.localtime()

        # Prevent bookings in the past
        if requested_date < now.date() or (
            requested_date == now.date() and requested_time < now.time()
        ):
            raise forms.ValidationError("You cannot book a date/time in the past.")

        # Opening hours
        weekday = requested_date.weekday()  # 0 = Monday
        if weekday <= 3:
            open_time = time(12, 0)
            close_time = time(21, 0)
        else:
            open_time = time(14, 0)
            close_time = time(23, 0)

        if not (open_time <= requested_time <= close_time):
            raise forms.ValidationError(
                f"On this day, bookings must be between {open_time.strftime('%H:%M')} and {close_time.strftime('%H:%M')}."
            )

        return cleaned_data