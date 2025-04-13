from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Ingredient, Recipe, RecipeIngredient, Profile, RecipeImage
 
class ProfileInline(admin.StackedInline):
     model = Profile
     can_delete = False
 
class UserAdmin(UserAdmin):
     inlines = [ProfileInline,]

class RecipeImageInline(admin.TabularInline):
     model = RecipeImage

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ('id', 'name', 'author', 'created_on', 'updated_on',)
    search_fields = ('name',)
    list_filter = ('name', 'author', 'created_on', 'updated_on',)
    inlines = [RecipeIngredientInline, RecipeImageInline]

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
