from django import forms
from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage
 
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']
      
class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['Recipe','Ingredient','quantity']
 
class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image','description']