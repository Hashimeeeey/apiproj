from django.db import models
from django.contrib.auth.models import User
class Recipe(models.Model):
    title=models.CharField(max_length=50)
    cuisine=models.CharField(max_length=50)
    meal_type=models.CharField(max_length=50)
    ingredients=models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Review(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)