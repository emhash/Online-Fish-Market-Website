from django.shortcuts import render

def loginpage(request):
    
    return render(request, "frontend/login.html")

def registration(request):

    return render(request, "frontend/register.html")