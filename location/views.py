from django.shortcuts import render
from .models import Location


def location_render(request):
    """
    Renders the location page
    """
    location = Location.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "location/location.html",
        {"location": location},
    )