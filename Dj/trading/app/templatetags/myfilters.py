from django import template
register = template.Library()


# mapping is dict here
@register.filter
def get(mapping, key):
    return mapping.get(key, '')