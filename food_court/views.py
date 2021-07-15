from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Food
# Create your views here.
def index(request):
    foods = Food.objects.all()
    return render(request,"food_court/index.html",{
        "foods":foods
    })

def food_detail(request,slug):
    
    food = Food.objects.get(slug=slug)

    return render(request,"food_court/food_detail.html",{
        "food":food
    })