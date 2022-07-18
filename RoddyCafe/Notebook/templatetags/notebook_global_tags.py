from django import template

register = template.Library()

@register.filter(name='escapejsString')
def escape_js_string(value): return str(value).replace(r'`',r'\`').replace(r'$',r'\$')

@register.filter(name='weekday')
def weekday(value):
    return {
        0 : lambda x: x + '一',
        1 : lambda x: x + '二',
        2 : lambda x: x + '三',
        3 : lambda x: x + '四',
        4 : lambda x: x + '五',
        5 : lambda x: x + '六',
        6 : lambda x: x + '日',
    }[value.weekday()]('周')
