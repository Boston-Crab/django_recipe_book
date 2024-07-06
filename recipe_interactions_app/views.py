from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from recipe_interactions_app.models import (
    RecipeIDFormApi,
    Like,
    Dislike,
    Comment,
)

def redirect_to_current_recipe(recipe_id):
    redirect(reverse('recipes:get_recipe_by_id', kwargs={'meal_id': recipe_id}))

@login_required
def like_recipe(request, recipe_id):
    # Check if it was disliked, when true - delete that dislike
    recipe = get_object_or_404(RecipeIDFormApi, recipe_id_from_api=recipe_id)
    is_liked_by_user = Dislike.objects.filter(user=request.user, recipe=recipe).first()
    if is_liked_by_user:
        undislike_recipe(request, recipe_id)

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
    # Check if it was liked, when true - delete that like
    recipe = get_object_or_404(RecipeIDFormApi, recipe_id_from_api=recipe_id)
    is_liked_by_user = Like.objects.filter(user=request.user, recipe=recipe).first()
    if is_liked_by_user:
        unlike_recipe(request, recipe_id)
    
    recipe = get_object_or_404(RecipeIDFormApi, recipe_id_from_api=recipe_id)
    if not Dislike.objects.filter(user=request.user, recipe=recipe).exists():
        Dislike.objects.create(user=request.user, recipe=recipe)
    return redirect(reverse('recipes:get_recipe_by_id', kwargs={'meal_id': recipe_id}))


@login_required
def undislike_recipe(request, recipe_id):
    recipe = get_object_or_404(RecipeIDFormApi, recipe_id_from_api=recipe_id)
    like = Dislike.objects.filter(user=request.user, recipe=recipe).first()
    if like:
        like.delete()
    return redirect(reverse('recipes:get_recipe_by_id', kwargs={'meal_id': recipe_id}))