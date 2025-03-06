from .models import Recipe
from django.shortcuts import render

def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, 'recipes_list.html', ctx)

def recipe_info(request, id):
    ctx = { 'recipe', Recipe.objects.get(id=id) }
    return render(request, 'recipe_info.html', ctx)