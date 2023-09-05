from django import template

register = template.Library()

@register.filter
def multiple(value, arg):
    try:
        value = float(value)
        arg = float(arg)
        if arg: return arg*value
    except: pass
    return ""


@register.filter
def divison(value, arg):
    try:
        value = float(value)
        arg = float(arg)
        if arg: return arg/value
    except: pass
    return ""