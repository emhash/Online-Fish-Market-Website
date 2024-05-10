from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.loginpage, name="loginpage"),
    path('sign-up/', views.registration, name="registration"),
    path('logout/', views.logout_view, name="logout_view"),
]
