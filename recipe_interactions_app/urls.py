from django.urls import path
from recipe_interactions_app.views import (
    like_recipe,
    unlike_recipe,
    dislike_recipe,
    undislike_recipe,
    leave_a_comment
)

app_name = 'recipe_interaction'

urlpatterns = [
    path('like/<int:recipe_id>/', like_recipe, name='like_recipe'),
    path('unlike/<int:recipe_id>/', unlike_recipe, name='unlike_recipe'),
    path('dislike/<int:recipe_id>/', dislike_recipe, name='dislike_recipe'),
    path('undislike/<int:recipe_id>', undislike_recipe, name='undislike_recipe'),
    path('make-a-comment/<int:recipe_id>/', leave_a_comment, name='commenting'),
]
