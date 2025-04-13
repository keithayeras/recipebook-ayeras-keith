from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy

from .forms import RecipeForm, IngredientForm, RecipeIngredientForm, RecipeImageForm
from django.views import View
from .models import Recipe, Ingredient, RecipeIngredient, Profile

class RecipesListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_info.html'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_add.html'
    success_url = reverse_lazy('ledger:recipe_add')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredient_form'] = IngredientForm()
        context['recipe_ingredient_form'] = RecipeIngredientForm()
        return context
    
    def form_valid(self, form):
        profile = get_object_or_404(Profile, user=self.request.user)
        form.instance.author = profile
        return super().form_valid(form)

class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'recipe_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_form'] = RecipeForm()
        context['recipe_ingredient_form'] = RecipeIngredientForm()
        return context
        
    def get_success_url(self):
        return reverse_lazy('ledger:ingredient_add')

class RecipeIngredientCreateView(LoginRequiredMixin, CreateView):
    model = RecipeIngredient
    form_class = RecipeIngredientForm
    template_name = 'recipe_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_form'] = RecipeForm()
        context['ingredient_form'] = IngredientForm()
        return context
        
    def get_success_url(self):
        return reverse_lazy('ledger:recipe_ingredient_add')

class RecipeAddImageView(LoginRequiredMixin, View):
    template_name = 'recipe_image_add.html'

    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        form = RecipeImageForm()
        return render(request, self.template_name, {'recipe': recipe, 'form': form})

    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        form = RecipeImageForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect(recipe.get_absolute_url())

        return render(request, self.template_name, {'recipe': recipe, 'form': form})
    
    def get_success_url(self):
        return reverse_lazy('ledger:recipe_image_add')

