from django.shortcuts import render
from .models import Menu


def menu_render(request):
    """
    Renders the Menu page with related items
    """
    menu = Menu.objects.all().order_by('-updated_on').first()

    if menu:
        items = menu.items.filter(is_active=True)
        starters = items.filter(category='Starter')
        mains = items.filter(category='Main')
        soups = items.filter(category='Soup')
        sides = items.filter(category='Side')
        desserts = items.filter(category__startswith='Dessert')
        drinks = items.filter(category__startswith='Drink')
    else:
        starters = mains = soups = sides = desserts = drinks = []

    return render(
        request,
        "menu/menu.html",
        {
            "menu": menu,
            "starters": starters,
            "mains": mains,
            "soups": soups,
            "sides": sides,
            "desserts": desserts,
            "drinks": drinks,
        },
    )
