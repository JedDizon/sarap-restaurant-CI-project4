from django.contrib import admin
from .models import Menu
from django_summernote.admin import SummernoteModelAdmin
from .models import MenuItem


@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'cost', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('category',)
    search_fields = ('name', 'description')