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
        
        the_user = authenticate(request ,email = userinfo, password = userpassword)
        
        if the_user is not None:
            try:
                login(request, the_user)
                next = request.GET.get('next')
                if next:
                    return redirect(next)
                return redirect("homepage")
            except Exception as e:
                messages.warning(request, f"ERROR: {e}")
        else:
            if User.objects.filter(email=userinfo).exists():
                messages.error(request, 'Incorrect password.')
            else:
                messages.error(request, 'Account does not exist!')

    return render(request, "frontend/login.html")


@login_required()
def logout_view(request):
    logout(request)
    return redirect("loginpage")



#  ===============    FORMS WORKS DOING HERE ===============
from django import forms
from django.contrib.auth.forms import UserCreationForm
class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model= User
        fields=['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:            
            self.fields[field].widget.attrs.update({
                'class': 'input', 
                'style': 'border:solid black 1px;',
                })

def registration(request):
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.role="customer"
            myform.save()
            messages.success(request, "Your account has been created!" )
            return redirect("loginpage")
    else:
        form=SignUpForm()

    return render(request, "frontend/register.html", {"form":form})
