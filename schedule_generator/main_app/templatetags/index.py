from django import template
register= template.Library()


@register.filter 
def get_item(Queryset,j):
    return Queryset.sun



@register.filter
def index(indexable, i):
    
    return indexable[i]


