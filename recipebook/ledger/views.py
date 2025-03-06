from .models import Recipe
from django.shortcuts import render

def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, 'recipes_list.html', ctx)

