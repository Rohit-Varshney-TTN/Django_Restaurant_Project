from django.db import models

class FoodItem(models.Model):
    CATEGORY_CHOICES = [
        ('veg', 'Vegetarian'),
        ('nonveg', 'Non-Vegetarian'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='veg')
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
