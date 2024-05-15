from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
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

# WORK <<--- HERE --------=========================
@login_required()
def cart_view(request, u_id):
    referring_url = request.META.get('HTTP_REFERER')
    print("---->>> One Item added to the cart <<<---- ")
    the_item = get_object_or_404(Fish, uid=u_id.strip())
    print(the_item)
    add_item = CartItem.objects.get_or_create(
        user= request.user.profile,
        fish= the_item,
        purchased= False,
    )
    orders_item = Order.objects.filter(
        user = request.user.profile,
        payment = False,
    )
    if orders_item.exists():
        # print(ordered_item)
        order = orders_item[0]
        if order.ordered_items.filter(fish = the_item).exists():
            add_item[0].quantity += 1
            print("Item increamented!")
            add_item[0].save()
            return HttpResponseRedirect(referring_url)
        else:
            order.ordered_items.add(add_item[0])
            print("Item added success")
            return HttpResponseRedirect(referring_url)
    else:
        order = Order(user = request.user.profile)
        order.save()
        order.ordered_items.add(add_item[0])
        print("Item added to cart")

    return redirect(referring_url)

@login_required()
def cart(request):
    profile = request.user.profile # as it is one to one field
    if Order.objects.filter(user = request.user.profile, payment=False).exists():
        cart_items = CartItem.objects.filter(user = profile, purchased = False)
        ordered = Order.objects.filter(user = profile, payment = False).first()
        context ={
            "cart":cart_items,
            "orders":ordered,
        }
        return render(request, "frontend/cart.html", context)
    else:
        print("You have no order.")
    return redirect("homepage")

def cart_plus(request,the_id):
    referring_url = request.META.get('HTTP_REFERER')
    try:
        item = get_object_or_404(CartItem, uid = the_id.strip())
        if Order.objects.filter(user = request.user.profile ,ordered_items=item, payment=False).exists():
                if item.purchased == False:
                    item.quantity += 1
                    item.save()
                    return redirect("cart")            
        else:
            print("Oops You have no oders!")
    except Exception as e:
        print('ERROR:--> ',e)

    return redirect(referring_url)

def cart_minus(request,the_id):
    referring_url = request.META.get('HTTP_REFERER')
    try:
        item = get_object_or_404(CartItem, uid = the_id.strip())
        if Order.objects.filter(user = request.user.profile ,ordered_items=item, payment=False).exists():
                if item.purchased == False:
                    if item.quantity > 1:
                        item.quantity -= 1
                        item.save()
                        return redirect("cart")
                    else:
                        print("No more item could be decrease!")
        else:
            print("Oops You have no oders!")
    except Exception as e:
        print('ERROR:--> ',e)

    return redirect(referring_url)


# ==============================================




# WORKING <<<<---=== HERE
def view_product(request, uid):
    the_product = get_object_or_404(Fish, uid = uid)
    
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