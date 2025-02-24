from django.shortcuts import render, HttpResponse

recipe_directory = {
    "recipes": [
        {
            "id": 1,
            "name": "Recipe 1",
            "ingredients": [
                {
                    "name": "tomato",
                    "quantity": "3pcs"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "pork",
                    "quantity": "1kg"
                },
                {
                    "name": "water",
                    "quantity": "1L"
                },
                {
                    "name": "sinigang mix",
                    "quantity": "1 packet"
                }
            ],
            "link": "/recipe/1"
        },
        {
            "id": 2,
            "name": "Recipe 2",
            "ingredients": [
                {
                    "name": "garlic",
                    "quantity": "1 head"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "vinegar",
                    "quantity": "1/2cup"
                },
                {
                    "name": "water",
                    "quantity": "1 cup"
                },
                {
                    "name": "salt",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "whole black peppers",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "pork",
                    "quantity": "1 kilo"
                }
            ],
            "link": "/recipe/2"
        }
    ]
}

def recipes_list(request):
    return render(request, 'recipes_list.html', recipe_directory)

def recipe_info(request, recipe_id):
    recipe = next((selection for selection in recipe_directory["recipes"] if selection["id"] == recipe_id), None)
    if recipe is None:
        return HttpResponse("Recipe not found", status=404)
    
    return render(request, 'recipe_info.html', {"recipe": recipe})
