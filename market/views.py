from django.shortcuts import render
from .models import *
def homepage(request):
    categories = Category.objects.all()
    fishes = Fish.objects.all()
    offers = Offer.objects.all()

    context ={
        "categories":categories,
        "fishes":fishes,
        "offers":offers,
    }
    return render(request, "frontend/index.html",context)
