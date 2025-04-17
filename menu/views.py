from django.shortcuts import render
from .models import Menu


def menu_render(request):
    """
    Renders the Menu page
    """
    menu = Menu.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "menu/menu.html",
        {"menu": menu},
    )