from django.urls import path
from .views import food_list, food_detail

urlpatterns = [
    path('', food_list, name='food-list'),  # URL for viewing all food items
    path('<int:food_id>/', food_detail, name='food-detail'),  # URL for viewing a specific food item
]
