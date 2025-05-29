from django.contrib import admin
from .models import Book, Reservation
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'guest_name', 'requested_date',
        'requested_time', 'seats', 'status')
    list_filter = ('status',)
    search_fields = ('user__username', 'guest_name')
    list_editable = ('status',)
