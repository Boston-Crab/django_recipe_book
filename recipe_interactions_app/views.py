from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from recipe_interactions_app.models import (
    RecipeIDFormApi,
    Like,
    Dislike,
    Comment,
)


@login_required
def like_recipe(request, recipe_id):
    recipe = get_list_or_404(Like, id=recipe_id)
    if not Like.objects.filter(user=request.user, recipe=recipe).exists():
        Like.objects.create(user=request.user, recipe=recipe)
    return render(request, 'search_app/recipe_details.html')


@login_required
def unlike_recipe(request, recipe_id):
    pass


@login_required
def dislike_recipe(request, recipe_id):
    pass


@login_required
def undislike_recipe(request, recipe_id):
    pass