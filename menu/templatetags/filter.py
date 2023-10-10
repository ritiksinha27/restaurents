from django import template

register = template.Library()

@register.filter
def floatmul(quantity, item_price):
    return quantity * item_price