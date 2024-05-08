from django.contrib import admin

from .models import Category,Offer,Fish,CartItem,Review,Favorite

admin.site.register(Category)
admin.site.register(Offer)
admin.site.register(Fish)
admin.site.register(CartItem)
admin.site.register(Review)
admin.site.register(Favorite)

