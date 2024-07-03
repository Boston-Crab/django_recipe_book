from django.urls import path
from search_app.views import get_recipies_by_name, index, get_recipe_by_id

urlpatterns = [
    path('api/get-recipes/', get_recipies_by_name, name="get_recipes"),
    path('api/get_recipe/<str:meal_id>/', get_recipe_by_id, name='get_recipe_by_id'),
    path("", index),
]
