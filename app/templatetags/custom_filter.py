from django import template

from app.models import Ticker

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key).get('content')

@register.simple_tag()
def get_ticker():
    return Ticker.objects.all()