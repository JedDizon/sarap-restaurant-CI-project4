from . import views
from django.urls import path

urlpatterns = [
    path('', views.location_render, name='location'),
]