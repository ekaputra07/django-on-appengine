from django import template
from markdown import markdown

register = template.Library()


@register.filter
def markdownize(text):
    return markdown(text)
