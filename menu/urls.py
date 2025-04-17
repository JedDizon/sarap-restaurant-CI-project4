from . import views
from django.urls import path

urlpatterns = [
    path('', views.menu_render, name='menu'),
]