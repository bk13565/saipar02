from django import template
register = template.Library()

def handlebars(value):
    return '%s' % value
register.filter('handlebars', handlebars)