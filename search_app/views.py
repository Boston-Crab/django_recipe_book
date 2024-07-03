import requests
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def get_recipies_by_name(request):
    search_term = request.GET.get('search_term', '')
    if request.method == "GET":
        url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={
            search_term}"
        response = requests.get(url)
        data = response.json()

        for meal in data['meals']:
            for i in range(1, 21):
                ingredient_key = f'strIngredient{i}'
                measurement_key = f'strMeasure{i}'
                if ingredient_key in meal and meal[ingredient_key] == '':
                    del meal[ingredient_key]
                if measurement_key in meal and meal[measurement_key] == '':
                    del meal[measurement_key]
                
        print(data)
        return HttpResponse(data['meals'])


def index(request):
    return render(request, "search_app/index.html")
