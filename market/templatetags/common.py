from django import template
from market.models import CartItem

register = template.Library()

@register.filter
def cart_data(user):
    carts = CartItem.objects.filter(user=user, purchased = False)

    if carts:
        item = carts.count()
        return item
    else:
        item = 0
        return item
