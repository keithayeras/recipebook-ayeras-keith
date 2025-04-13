from django import forms
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage
 
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']
      
class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['Recipe','Ingredient','quantity']
 
class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image','description']