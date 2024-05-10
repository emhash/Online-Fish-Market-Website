from django.shortcuts import render, redirect, HttpResponseRedirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import *
from .shortcuts import ObjectMaster
from .filter import FishFilter

def homepage(request):
    categories = Category.objects.all()
    fishes = Fish.objects.all().order_by('price')
    offers = Offer.objects.all()

    obj = ObjectMaster(request=request,the_query=fishes)
    pg_obj = obj.Paginate(no_of_object=15)

    context ={
        "categories":categories,
        "fishes":pg_obj,
        "offers":offers,
    }
    return render(request, "frontend/index.html",context)

# WORK <<--- HERE
@login_required()
def cart_view(request, uid):
    referring_url = request.META.get('HTTP_REFERER')
    # print(uid)

    return redirect(referring_url)

# WORKING <<<<---=== HERE
def view_product(request, uid):
    the_product = get_list_or_404(Fish, uid = uid)
    
    referring_url = request.META.get('HTTP_REFERER')

    context = {
        "fish":the_product,
    }
    return render(request, "frontend/view_product.html", context)

def products(request):
    fishes = Fish.objects.all().order_by('price')

    obj = ObjectMaster(request=request,the_query=fishes)
    search,filtered = obj.Searching(FilteredQuery=FishFilter)
    pg = obj.Paginate(query=filtered ,no_of_object=50)

    context ={
        "fishes":pg,
        "searching":search,
    }
    return render(request, "frontend/products.html", context)