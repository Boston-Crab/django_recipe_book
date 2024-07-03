from django.urls import path
from search_app.views import get_recipies_by_name, index

urlpatterns = [
    path('api/get-recipes/', get_recipies_by_name, name="get_recipes"),
    path("", index)
]
