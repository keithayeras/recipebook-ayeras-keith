from django.urls import path
from .views import RecipesListView, RecipeDetailView

app_name = 'ledger'

urlpatterns = [
    path('recipes/list/', RecipesListView.as_view(), name='recipes_list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_info'),
]