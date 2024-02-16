from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, args):
  class_ = value.field.widget.attrs.get('class','')
  class_ += args
  value.field.widget.attrs.update(
    {'class':class_,
      'placeholder': value.field.label
    })
  return value