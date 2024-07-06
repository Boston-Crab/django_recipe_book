from django.db import models
from django.contrib.auth.models import User

class RecipeIDFormApi(models.Model):
    recipe_id_from_api = models.IntegerField(unique=True)

    def __str__(self):
        return self.recipe_id_from_api
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    recipe = models.ForeignKey(RecipeIDFormApi, on_delete=models.CASCADE)
    liking_time = models.DateTimeField(auto_now_add=True)

    # to stop from liking more than 1 time:
    class Meta:
        unique_together = ('user', 'article')
    
    def __str__(self):
        return f"User: {self.user} - LIKED - Recipe: {self.recipe}"
    
class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    recipe = models.ForeignKey(RecipeIDFormApi, on_delete=models.CASCADE)
    liking_time = models.DateTimeField(auto_now_add=True)

    # to stop from disliking more than 1 time:
    class Meta:
        unique_together = ('user', 'article')
    
    def __str__(self):
        return f"User: {self.user} - DISLIKED - Recipe: {self.recipe}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(RecipeIDFormApi, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=1000)
    comment_date = models.DateTimeField(auto_now_add=True)
