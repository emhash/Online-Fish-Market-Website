from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

from payment.views import payment_process
from adminpanel.forms import ContactUsMessageForm
from .models import *
from .shortcuts import ObjectMaster
from .filter import FishFilter

def homepage(request):    
    categories = Category.objects.all()
    fishes = Fish.objects.all().order_by('price')
    offers = Offer.objects.all()
    if request.method=="POST":
        form=ContactUsMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has reached to us. Thank you!")
            return redirect(request.path)                
    else:
        form=ContactUsMessageForm()
    obj = ObjectMaster(request=request,the_query=fishes)
    pg_obj = obj.Paginate(no_of_object=15)

    context ={
        "categories":categories,
        "fishes":pg_obj,
        "offers":offers,
        "form":form,
    }
    return render(request, "frontend/index.html",context)

# WORK <<--- HERE --------=========================
@login_required()
def cart_view(request, u_id):
    referring_url = request.META.get('HTTP_REFERER')
    # print("---->>> One Item added to the cart <<<---- ")
    the_item = get_object_or_404(Fish, uid=u_id.strip())
    # print(the_item)
    add_item = CartItem.objects.get_or_create(
        user= request.user.profile,
        fish= the_item,
        purchased= False,
    )
    add_item[0].quantity+=1
    messages.success(request, "Your fish has been added to cart!")
    '''
    Below the old logic that was implement for pay with the entire card that 
    saves with onw order table with the cart items. 
    But Now i made the logic change so that user can select the cart
    items and proceed to pay.
    '''
    # orders_item = Order.objects.filter(
    #     user = request.user.profile,
    #     payment = False,
    # )
    # if orders_item.exists():
    #     # print(ordered_item)
    #     order = orders_item[0]
    #     if order.ordered_items.filter(fish = the_item).exists():
    #         add_item[0].quantity += 1
    #         # print("Item increamented!")
    #         add_item[0].save()
    #         return HttpResponseRedirect(referring_url)
    #     else:
    #         order.ordered_items.add(add_item[0])
    #         # print("Item added success")
    #         return HttpResponseRedirect(referring_url)
    # else:
    #     order = Order(user = request.user.profile)
    #     order.save()
    #     order.ordered_items.add(add_item[0])
    #     # print("Item added to cart")

    return redirect(referring_url)

@login_required()
def cart(request):
    profile = request.user.profile # as it is one to one field    
    cart_items = CartItem.objects.filter(user = profile, purchased = False)
    referring_url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        selected_items = request.POST.getlist('selected_items')
        
        if selected_items:
            # Store selected items in the session
            request.session['selected_items'] = selected_items
            return redirect("process")
        else:
            messages.warning(request, "Please select your product to go pay")
    
    if cart_items.exists():
        context ={
            "cart":cart_items,
            
        }
        return render(request, "frontend/cart.html", context)
    else:
        messages.warning(request,"You have no items in cart!")
    return redirect(referring_url)

@login_required()
def cart_plus(request,the_id):
    referring_url = request.META.get('HTTP_REFERER')
    try:
        item = get_object_or_404(CartItem, uid = the_id.strip())
        
        item.quantity += 1
        item.save()
        return redirect("cart")
    except Exception as e:
        print('ERROR:--> ',e)

    return redirect(referring_url)

@login_required()
def cart_minus(request,the_id):
    referring_url = request.META.get('HTTP_REFERER')
    try:
        item = get_object_or_404(CartItem, uid = the_id.strip())
        
        if item.quantity > 1:
            item.quantity -= 1
            item.save()

            return redirect("cart")
        else:
            messages.warning(request,"No more item could be decrease!")
    except Exception as e:
        messages.error(request, e)

    return redirect(referring_url)


# ==============================================

# WORKED <<<<---=== 
def delete_cart_product(request, puid):
    the_cart = get_object_or_404(CartItem, uid=puid.strip())
    try:
        the_cart.delete()
    except:
        print("Cant delete due to some error!")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required()
def view_product(request, uid):
    the_product = get_object_or_404(Fish, uid = uid)
    
    referring_url = request.META.get('HTTP_REFERER')

    context = {
        "fish":the_product,
    }
    return render(request, "frontend/view_product.html", context)

@login_required()
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

@login_required()
def my_orders(request):
    profile=request.user.profile
    orders = Order.objects.filter(user=profile, payment=True)
    context ={
        "orders":orders,
    }
    return render(request, "frontend/my_orders.html", context)



