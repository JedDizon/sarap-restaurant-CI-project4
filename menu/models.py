from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('Starter', 'Starter'),
        ('Main', 'Main'),
        ('Soup', 'Soup'),
        ('Side', 'Side'),
        ('Dessert - Traditional', 'Dessert - Traditional'),
        ('Dessert - Other', 'Dessert - Other'),
        ('Drink - Hot', 'Drink - Hot'),
        ('Drink - Cocktail', 'Drink - Cocktail'),
        ('Drink - Nonalcoholic', 'Drink - Nonalcoholic'),
        ('Drink - Spirit', 'Drink - Spirit'),
        ('Drink - Beer', 'Drink - Beer'),
        ('Drink - Mixer', 'Drink - Mixer'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_active = models.BooleanField(default=True)
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='items')

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.category})"
