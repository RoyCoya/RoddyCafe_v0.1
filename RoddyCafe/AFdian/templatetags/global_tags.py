from django import template

register = template.Library()

@register.filter(name='replace_bool_capital')
def replace_bool_capital(value): return str(value).replace("False", "false")