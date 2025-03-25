from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
from food.models import FoodItem
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, food_id):
    food_item = get_object_or_404(FoodItem, id=food_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, food_item=food_item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart-view')

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def remove_from_cart(request, food_id):
    cart_item = get_object_or_404(Cart, user=request.user, food_item_id=food_id)
    cart_item.delete()
    return redirect('cart-view')
