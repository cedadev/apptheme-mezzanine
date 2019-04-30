from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def portfolioitem_in_category(things, category):
    return things.filter(categories__in=[category,])

@register.filter
@stringfilter
def de_b(value):
    ''' If string value is prefixed as a bytecode (b'somestring', remove the wrapping b'')'''
    return str(value.encode('utf-8'))[2:-1]