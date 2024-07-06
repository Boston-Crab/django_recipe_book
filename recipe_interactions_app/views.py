from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from recipe_interactions_app.models import (
    RecipeIDFormApi,
    Like,
    Dislike,
    Comment,
)


@login_required
def like_recipe(request, recipe_id):
    recipe = get_object_or_404(RecipeIDFormApi, recipe_id_from_api=recipe_id)
    if not Like.objects.filter(user=request.user, recipe=recipe).exists():
        Like.objects.create(user=request.user, recipe=recipe)
    return redirect(reverse('recipes:get_recipe_by_id', kwargs={'meal_id': recipe_id}))


@login_required
def unlike_recipe(request, recipe_id):
    recipe = get_object_or_404(RecipeIDFormApi, recipe_id_from_api=recipe_id)
    like = Like.objects.filter(user=request.user, recipe=recipe).first()
    if like:
        like.delete()
    return redirect(reverse('recipes:get_recipe_by_id', kwargs={'meal_id': recipe_id}))
    


@login_required
def dislike_recipe(request, recipe_id):
    pass


@login_required
def undislike_recipe(request, recipe_id):
    pass