from django import template
from market.models import CartItem, Order

register = template.Library()

@register.filter
def cart_data(profile):
    if profile:
        carts = CartItem.objects.filter(user=profile, purchased = False)        
        if carts:
            item = carts.count()
            return item
        else:
            return 0
    else:
        return 0
