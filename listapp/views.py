from django.shortcuts import render
import json
from .models import Lista
from django.http import JsonResponse

# Create your views here.
def home_view(request, *args, **kwargs):

    elemek = Lista.objects.all()
    kontextus = {
    "a": 123,
    "b": "blablabla",
    "l": [1,3,5,7,9],
    }
    if (request.method == "POST"):
        array = json.load(request)
        response = Lista.create(array)
        if(response['response'] == True):
            data = {
                'response': 'OK',
                'massage': response['massage'],
            }
        elif(response['response'] =='nemjó'):
            data = {
                'response': 'Már van ilyen meglévő elem',
                'massage': 'Már van ilyen meglévő elem',
            }
        else:
            data = {
                'response': response['response'],
                'massage': response['massage'],
            }
        return JsonResponse(data)
        print("POST request érkezett!" )
    return render(request, "home.html", kontextus) 

def torles(request, *args, **kwargs):
    array = json.load(request)
    response = Lista.delete(array)
        if(response['response'] == True):
            data = {
                'response': 'OK',
                'massage': response['massage'],
            }
        elif(response['response'] =='nemtalált'):
            data = {
                'response': 'Nem talált ilyet',
                'massage': 'Nem talált ilyet',
            }
        else:
            data = {
                'response': response['response'],
                'massage': response['massage'],
            }
        return JsonResponse(data)
        print("POST request érkezett!: törlés" )