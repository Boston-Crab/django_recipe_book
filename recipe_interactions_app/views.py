from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def like_recipe(request, recipe_id):
    pass


@login_required
def unlike_recipe(request, recipe_id):
    pass


@login_required
def dislike_recipe(request, recipe_id):
    pass


@login_required
def undislike_recipe(request, recipe_id):
    pass