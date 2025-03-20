from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    Bio = models.CharField(max_length=255)

class Ingredient(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.name)])

class Recipe(models.Model):
    Name = models.CharField(max_length=100)
    Author = models.CharField(max_length=50)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    UpdatedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.name)])

class RecipeIngredient(models.Model):
    Quantity = models.CharField(max_length=100)
    Ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe'
    )
    Recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
