from django import template
from django.template.defaultfilters import stringfilter
from bee.models import UserBee
register = template.Library()

@register.filter
@stringfilter
def lower(value):
    return value.lower()


@register.filter
def can_admin(value, pr_id):
    if isinstance(value, UserBee):
        return value.has_admin_permission(pr_id)
    else:
        return False

@register.filter
def can_write(value, pr_id):
    if isinstance(value, UserBee):
        return value.has_write_permission(pr_id)
    else:
        return False
@register.filter
def can_read(value, pr_id):
    if isinstance(value, UserBee):
        return value.has_read_permission(pr_id)
    else:
        return False