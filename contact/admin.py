from django.contrib import admin
from .models import Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Contact)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)