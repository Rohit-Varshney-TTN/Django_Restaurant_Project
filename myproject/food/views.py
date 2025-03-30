from django.shortcuts import render, get_object_or_404
from .models import FoodItem

def food_list(request):
    """
    View to display the list of food items with search and category filtering.
    """
    query = request.GET.get('q', '')  # Get search query
    category = request.GET.get('category', '')  # Get category filter (Veg/Non-Veg)

    # Start with all food items
    foods = FoodItem.objects.all()

    # Filter by name if query is provided
    if query:
        foods = foods.filter(name__icontains=query)

    # Filter by category if selected
    if category and category != 'all':
        foods = foods.filter(category=category)

    return render(request, 'food/food_list.html', {'foods': foods, 'query': query, 'selected_category': category})


def food_detail(request, food_id):
    """
    View to display the details of a specific food item.
    """
    food = get_object_or_404(FoodItem, id=food_id)
    return render(request, 'food/food_detail.html', {'food': food})
