from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from sslcommerz_lib import SSLCOMMERZ 
from django.http import JsonResponse
from django.contrib import messages
import uuid

# from decimal import Decimal
# from sslcommerz_python.payment import SSLCSession
# from aamarpay.aamarpay import aamarPay

from .forms import BillingAddressForm
from .models import BillingAddress
from market.models import CartItem, Order, Fish
from .decoretor import bill_checker

@login_required
def payment_process(request):
    profile = request.user.profile
    bill = BillingAddress.objects.get_or_create(owner=profile,)[0]

    items = request.session.get('selected_items')
    products = []
    for p_uid in items:
        products.append(CartItem.objects.filter(uid=p_uid.strip(), user=profile)[0])
    
    # Clear the session
    # request.session.pop('selected_items', None)

    if request.method == "POST":        
        form=BillingAddressForm(request.POST,instance=bill)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Billing address has been updated!")
            return redirect(request.path)
                
    # if request is GET-->
    else:
        form=BillingAddressForm(instance=bill)
    cost = sum([x.subtotal() for x in products])
    context={"form":form, "products":products, "cost":cost}
    return render(request,"frontend/pay/process.html", context)

@login_required
# @bill_checker()
def payment_session(request):
    profile=request.user.profile
    bill = get_object_or_404(BillingAddress, owner=profile)
    if not bill.is_fully_filled():
        messages.error(request,"Please fill up your billing address first!")
        return redirect("process")
    
    sslcz = SSLCOMMERZ({
        'store_id': 'toito66a299fe9adb2',
        'store_pass': 'toito66a299fe9adb2@ssl',
        'issandbox': True  # Change to False in production
    })

    cart_products = request.session.get('selected_items')
    
    products = []
    for p_uid in cart_products:
        products.append(CartItem.objects.filter(uid=p_uid.strip(), user=profile)[0])
  
    post_body = {}

    post_body['success_url'] = request.build_absolute_uri(reverse('success'))
    post_body['fail_url'] = request.build_absolute_uri(reverse('fail'))
    post_body['cancel_url'] = request.build_absolute_uri(reverse('cancel'))
    
    # -- payment_notification --
    # post_body['ipn_url'] = request.build_absolute_uri(reverse('ipn'))
    cost = sum([x.subtotal() for x in products])
    quantity = sum([x.quantity for x in products])
    post_body['total_amount'] = f"{cost}"
    post_body['currency'] = "BDT"
    post_body['product_category'] = "mixed"
    post_body['product_name'] = f"Mixed Fishes"
    post_body['num_of_item'] = f"{quantity}"
    post_body['shipping_method'] = 'NO'
    
    name=profile.name
    email=request.user.email
    phone_no=profile.bill_owner.phone_no
    area=profile.bill_owner.area
    city=profile.bill_owner.city
    country=profile.bill_owner.country
    post_code=profile.bill_owner.post_code
    
    post_body['cus_name'] = f'{name}'
    post_body['cus_email'] = f'{email}'
    post_body['cus_phone'] = f'{phone_no}'
    post_body['cus_add1'] = f'{area}'
    post_body['cus_city'] = f'{city}'
    post_body['cus_country'] = f'{country}'
    post_body['postcode'] = f'{post_code}'

    post_body['product_profile'] = "general"
    post_body['tran_id'] = f"{uuid.uuid4()}"
    
    # post_body['multi_card_name'] = ""
    # post_body['emi_option'] = 0
    

    response = sslcz.createSession(post_body)
    
    
    if response['status'] == 'SUCCESS':
        return redirect(response['GatewayPageURL'])
    else:
        return JsonResponse(response)


from django.views.decorators.csrf import csrf_protect, csrf_exempt
import time
# @login_required()
@csrf_exempt
def success(request):    
    if request.POST or request.post:
        data = request.POST
        if data['status'] == 'VALID':
            val_id = data['val_id']  
            trans_id = data['tran_id']  
            return redirect("shopping", val_id=val_id, trans_id=trans_id)
            
    return render(request, "frontend/pay/success.html")

@login_required
def shopping(request,val_id, trans_id):
    try:
        profile=request.user.profile
        items = request.session.get('selected_items')            
        orders = Order.objects.create(user=profile)
        orders.payment = True
        orders.payment_id = val_id.strip()
        orders.order_id = trans_id.strip()
        for p_uid in items:
            this_item =CartItem.objects.filter(uid=p_uid.strip(), user=profile)[0]
            orders.ordered_items.add(this_item)
            this_item.purchased = True
            this_item.save()
        orders.save()
        messages(request, "Congrats! Your order took place.")
    except Exception as e:
        messages.warning(request, f"{e}")

    return redirect("cart")

@csrf_exempt
def cancel(request):
    if request.POST or request.post:
        data = request.POST
        print(data['status'])
        for i in data:
            print(i , "==>> ",[data[i]])
    return render(request, "frontend/pay/cancel.html")

# @login_required
@csrf_exempt
def fail(request):
    return render(request, "frontend/pay/fail.html")


@login_required
def complete(request):
    return render(request, "frontend/pay/complete.html")