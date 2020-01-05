from django import template
import random

from django.urls import resolve, reverse, Resolver404
from django.utils.translation import get_language, activate

from app.models import Ticker, Quote, Menu
from settings import settings

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.simple_tag()
def get_ticker():
    return Ticker.objects.all()


@register.simple_tag()
def get_quote():
    quote = random.choice(Quote.objects.all())
    return quote

@register.simple_tag()
def get_menu_list():
    menulist = Menu.objects.all()
    print(menulist.count())
    return menulist

@register.simple_tag(takes_context=True)
def change_lang(context, lang=None, *args, **kwargs):
    """
    Get active page's url by a specified language
    Usage: {% change_lang 'en' %}
    """
    path = context['request'].path
    full_path = context['request'].get_full_path()
    try:
        url_parts = resolve(path)
        cur_language = get_language()
        try:
            activate(lang)
            url = reverse(url_parts.view_name, kwargs=url_parts.kwargs)
            activate(cur_language)
            parameters = "?{0}".format(full_path.split('?')[1]) if len(full_path.split('?')) == 2 else ""
            return "{0}{1}".format(url, parameters)
        except Exception:
            pass
    except Resolver404:
        pass
    return full_path

@register.simple_tag()
def get_languages():
    return settings.LANGS