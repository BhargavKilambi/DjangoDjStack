from django import template


register = template.Library()

@register.filter(name='split_tags')
def split_tags(value,args):
	return value.split(',')