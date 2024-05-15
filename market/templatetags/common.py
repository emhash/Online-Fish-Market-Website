from django import template
from market.models import CartItem, Order

register = template.Library()

@register.filter
def cart_data(user):
    if Order.objects.filter(user = user, payment=False).exists():
        carts = CartItem.objects.filter(user=user, purchased = False)
    else:
        carts = None

    if carts:
        item = carts.count()
        return item
    else:
        item = 0
        return item
