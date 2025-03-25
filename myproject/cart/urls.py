from django.urls import path
from .views import add_to_cart, view_cart, remove_from_cart

urlpatterns = [
    path('add/<int:food_id>/', add_to_cart, name='add-to-cart'),
    path('', view_cart, name='cart-view'),
    path('remove/<int:food_id>/', remove_from_cart, name='remove-from-cart'),
]
