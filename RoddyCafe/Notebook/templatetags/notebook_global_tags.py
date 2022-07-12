from django import template

register = template.Library()

@register.filter(name='escapejsString')
def escape_js_string(value): return str(value).replace(r'`',r'\`').replace(r'$',r'\$')