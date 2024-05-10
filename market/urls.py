from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path("cart/item/<str:uid>", views.cart_view, name="cart_view" ),
    path("product/item/<str:uid>", views.view_product, name="view_product" ),
    path("products/", views.products, name="products" ),
]
