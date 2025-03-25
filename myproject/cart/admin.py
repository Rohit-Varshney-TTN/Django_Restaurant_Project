from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'food_item', 'quantity', 'total_price')

admin.site.register(Cart, CartAdmin)
