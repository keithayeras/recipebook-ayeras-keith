from django.urls import path
from .views import RecipesListView, RecipeDetailView, RecipeCreateView, IngredientCreateView, RecipeIngredientCreateView, RecipeAddImageView

app_name = 'ledger'

urlpatterns = [
    path('recipes/list/', RecipesListView.as_view(), name='recipes_list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_info'),
    path('recipes/add/', RecipeCreateView.as_view(), name='recipe_add'),
    path('recipes/add-ingredient/', IngredientCreateView.as_view(), name='ingredient_add'),
    path('recipes/add-recipe-ingredient/', RecipeIngredientCreateView.as_view(), name='recipe_ingredient_add'),
    path('recipes/<int:pk>/add-image/', RecipeAddImageView.as_view(), name='recipe_image_add'),
]