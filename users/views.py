from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from . models import User


def loginpage(request):
    if request.method == "POST":
        userinfo = request.POST['userinfo']
        userpassword = request.POST["userpassword"]
        if not (userinfo and userpassword):
            messages.warning(request, "Fill up both fields!")
            return redirect(request.path)
        print(userinfo)
        print(userpassword)
        the_user = authenticate(request ,email = userinfo, password = userpassword)
        print(the_user)
        if the_user is not None:
            try:
                login(request, the_user)
                return redirect("homepage")
            except Exception as e:
                messages.warning(request, f"ERROR: {e}")
        else:
            if User.objects.filter(email=userinfo).exists():
                messages.error(request, 'Incorrect password.')
            else:
                messages.error(request, 'Account does not exist!')

    return render(request, "frontend/login.html")

def registration(request):

    return render(request, "frontend/register.html")

@login_required()
def logout_view(request):
    logout(request)
    return redirect("loginpage")