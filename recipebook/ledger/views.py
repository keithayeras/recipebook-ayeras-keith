from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, get_object_or_404, render

from .forms import RecipeForm, RecipeIngredientForm, RecipeImageForm
from django.views import View
from .models import Recipe

class RecipesListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_info.html'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except ObjectDoesNotExist:

            return redirect('recipe_list')

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['ingredient_form'] = RecipeIngredientForm(self.request.POST)
        else:
            context['ingredient_form'] = RecipeIngredientForm()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        ingredient_form = context['ingredient_form']

        if ingredient_form.is_valid():
            form.instance.author = self.request.user
            self.object = form.save()

            ingredient = ingredient_form.save(commit=False)
            ingredient.recipe = self.object
            ingredient.save()

            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

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