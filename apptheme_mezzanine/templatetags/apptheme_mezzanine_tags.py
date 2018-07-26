from django import template

register = template.Library()

@register.filter
def portfolioitem_in_category(things, category):
    return things.filter(categories__in=[category,])