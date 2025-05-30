from django.test import TestCase, Client
from django.urls import reverse
from .models import Menu, MenuItem


class MenuTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu = Menu.objects.create(
            title="Summer Menu",
            content="Our freshest seasonal offerings."
        )

        self.item1 = MenuItem.objects.create(
            name="Spring Rolls",
            description="Crispy rolls with veggies",
            cost=5.50,
            category="Starter",
            is_active=True,
            menu=self.menu
        )

        self.item2 = MenuItem.objects.create(
            name="Beef Steak",
            description="Grilled steak with herbs",
            cost=18.00,
            category="Main",
            is_active=False,
            menu=self.menu
        )

    def test_menu_str(self):
        """Test string representation of Menu"""
        self.assertEqual(str(self.menu), "Summer Menu")

    def test_menu_item_str(self):
        """Test string representation of MenuItem"""
        self.assertEqual(str(
            self.item1), "Spring Rolls (Starter)")

    def test_menu_items_by_category(self):
        """Test items are correctly categorized"""
        response = self.client.get(reverse("menu"))
        starters = response.context['starters']
        mains = response.context['mains']

        self.assertIn(self.item1, starters)
        self.assertNotIn(self.item2, mains)
