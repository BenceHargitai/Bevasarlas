from django.shortcuts import render

from .models import Lista
# Create your views here.
def home_view(request, *args, **kwargs):

    elemek = Lista.objects.all()
    kontextus = {
    "a": 123,
    "b": "blablabla",
    "l": [1,3,5,7,9],
    }
    return render(request, "home.html", kontextus) 