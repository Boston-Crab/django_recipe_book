from django.urls import path
from search_app.views import get_recipies_by_name, index, get_recipe_by_id

app_name = "recipes"

urlpatterns = [
    path('recipes-search', get_recipies_by_name, name="get_recipes"),
    path('recipe-info/<str:meal_id>/', get_recipe_by_id, name='get_recipe_by_id'),
    path("", index, name='index'),
]
