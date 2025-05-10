from . import views
from django.urls import path

# urlpatterns = [
#     path('', #views.about_me, name='about'),
#     path('', views.about_view, name='about'),
# ]

urlpatterns = [
    path('', views.about_view, name='about'),
]