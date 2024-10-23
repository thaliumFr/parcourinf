from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def lien_ariane(lien: str):
    lien = lien.strip("/")
    liens = lien.split("/")
    res = ""

    for tag in liens:
        res += f'<li><a class="fr-breadcrumb__link" href="/">{tag}</a></li>'
    return mark_safe(res)
