from django import template

from app.models import Ticker

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key).get('content')

@register.tag
def get_ticker(wtf):
    return Ticker.objects.all()