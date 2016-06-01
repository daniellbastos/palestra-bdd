from django import template
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def render_form(form, included_or_ignored=None):
    include = False
    ignore = False
    names = []
    if included_or_ignored:
        if included_or_ignored.startswith('-'):
            ignore = True
            included_or_ignored = included_or_ignored[1:]
        else:
            include = True
        names = included_or_ignored.split(',')

    s = force_unicode(form.non_field_errors())
    for field in form.hidden_fields():
        s += force_unicode(field)

    for field in form.visible_fields():
        if include and not field.name in names:
            continue
        if ignore and field.name in names:
            continue
        s += render_field(field)
    return mark_safe(s)


@register.filter
def render_field(field):
    slug = field.field.widget.__class__.__name__.lower()
    templates = [
        'forms/{0}.html'.format(slug),
        'forms/field.html'
    ]
    return template.loader.render_to_string(
        templates, {'field': field, 'slug': slug})
