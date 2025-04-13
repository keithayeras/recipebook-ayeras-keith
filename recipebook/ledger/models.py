from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.name)])
    
    class Meta:
        constraints = [models.UniqueConstraint(fields=['name'], name='uniqueIngredient')]

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recipes', default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_info', args=[str(self.pk)])
    
    class Meta:
        ordering = ['name']
        constraints = [models.UniqueConstraint(fields=['name','author'], name='uniqueNamePerAuthor')]

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
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

    class Meta:
        constraints = [models.UniqueConstraint(fields=['Recipe','Ingredient'], name='uniqueIngredientPerRecipe')]

class RecipeImage(models.Model):
    image = models.ImageField(upload_to='recipe_images/', null=False)
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return f"Image for {self.recipe.name}"
    
    def get_absolute_url(self):
         return reverse('recipe_image_add',args=[self.recipe.pk])