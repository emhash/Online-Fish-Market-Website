from django.contrib.auth.decorators import login_required
from .models import BillingAddress
from django.shortcuts import redirect, HttpResponse

def bill_checker(var=None):
    def outside(viewfunc):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                profile = request.user.profile
                bill = BillingAddress.objects.get_or_create(owner=profile)
                if bill.is_fully_filled():
                    return viewfunc(request, *args, **kwargs)
                else:
                    return redirect("process")
            else:
                print("Login First")
                return redirect("homepage")
            
        return wrapper
    return outside



# def login_requirements():
#     def outer(function_in_view):
#         @login_required
#         def wrapper_func(request, *args, **kwargs):
#             # wrapper function that bind with logic
#             pass
#         return wrapper_func
#     return outer
