import requests
from django.shortcuts import render
from django.http import HttpResponse
from recipe_book.settings import MEAL_API_URL



def get_recipies_by_name(request):
    search_term = request.GET.get('search_term', '')
    if request.method == "GET":
        url = f"{MEAL_API_URL}/search.php?s={
            search_term}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['meals'] is not None:
                context = {'data': data['meals']}

                return render(request, "search_app/search_results.html", context)
            else:
                return render(request, "search_app/index.html", {'message': f"No meals found for '{search_term}'. Try something else."})
        else:
            return render(request, "search_app/index.html")
        
def get_recipe_by_id(request, meal_id):
    url = f'{MEAL_API_URL}//lookup.php?i={meal_id}'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if data['meals'] is not None:
            ingredients_list = []
            
            for meal in data['meals']:
                for i in range(1, 21):
                    ingredient_key = f'strIngredient{i}'
                    measurement_key = f'strMeasure{i}'
                    
                    if ingredient_key in meal and meal[ingredient_key] and measurement_key in meal and meal[measurement_key]:
                        ingredients_list.append(
                            f"{meal[ingredient_key]} - {meal[measurement_key]}"
                        )

            context = {
                'meal_id': data['meals'][0]['idMeal'],
                'meal_title': data['meals'][0]['strMeal'],
                'meal_category': data['meals'][0]['strCategory'],
                'meal_culture': data['meals'][0]['strArea'],
                'meal_instructions': data['meals'][0]['strInstructions'],
                'meal_image': data['meals'][0]['strMealThumb'],
                'meal_ingredients': ingredients_list,
                'meal_source': data['meals'][0]['strSource'],
            }

            return render(request, 'search_app/recipe_details.html', context)


def index(request):
    return render(request, "search_app/index.html")
