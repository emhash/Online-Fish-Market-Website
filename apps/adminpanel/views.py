from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from django.urls import reverse

def dashboard(request):
    return render(request, "admin/pages/index.html")