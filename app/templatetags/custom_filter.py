from django import template
import random
from app.models import Ticker, Quote

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key).get('content')


@register.simple_tag()
def get_ticker():
    return Ticker.objects.all()


@register.simple_tag()
def get_quote():
    quote = random.choice(Quote.objects.all())
    return quote