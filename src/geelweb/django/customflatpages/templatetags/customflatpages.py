from django import template
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from geelweb.django.customflatpages.models import CustomFlatPage

register = template.Library()

class CustomFlatpageNode(template.Node):
    def __init__(self, context_name, starts_with=None, user=None, emplacement=None):
        self.context_name = context_name
        if starts_with:
            self.starts_with = template.Variable(starts_with)
        else:
            self.starts_with = None
        if user:
            self.user = template.Variable(user)
        else:
            self.user = None
        if emplacement:
            self.emplacement = template.Variable(emplacement)
        else:
            self.emplacement = None

    def render(self, context):
        if 'request' in context:
            site_pk = get_current_site(context['request']).pk
        else:
            site_pk = settings.SITE_ID
        flatpages = CustomFlatPage.objects.filter(sites__id=site_pk)
        # If a prefix was specified, add a filter
        if self.starts_with:
            flatpages = flatpages.filter(
                url__startswith=self.starts_with.resolve(context))

        # If the provided user is not authenticated, or no user
        # was provided, filter the list to only public flatpages.
        if self.user:
            user = self.user.resolve(context)
            if not user.is_authenticated():
                flatpages = flatpages.filter(registration_required=False)
        else:
            flatpages = flatpages.filter(registration_required=False)

        if self.emplacement:
            flatpages = flatpages.filter(emplacement=self.emplacement.resolve(context))

        # sort by order field
        flatpages = flatpages.order_by('order')

        context[self.context_name] = flatpages
        return ''


@register.tag
def get_customflatpages(parser, token):
    """
    Retrieves all flatpage objects available for the current site and
    visible to the specific user (or visible to all users if no user is
    specified). Populates the template context with them in a variable
    whose name is defined by the ``as`` clause.

    An optional ``for`` clause can be used to control the user whose
    permissions are to be used in determining which flatpages are visible.

    An optional argument, ``starts_with``, can be applied to limit the
    returned flatpages to those beginning with a particular base URL.
    This argument can be passed as a variable or a string, as it resolves
    from the template context.

    Syntax::

        {% get_customflatpages ['url_starts_with'] [for user] [at emplacement] as context_name %}

    Example usage::

        {% get_customflatpages as flatpages %}
        {% get_customflatpages '/about/' as about_pages %}
        {% get_customflatpages prefix as about_pages %}
        {% get_customflatpages for someuser as flatpages %}
        {% get_customflatpages at some_emplacement as flatpages %}
        {% get_customflatpages '/about/' for someuser as about_pages %}
        {% get_customflatpages '/about/' at some_emplacement as about_pages %}
        {% get_customflatpages prefix at some_emplacement as about_pages %}
        {% get_customflatpages for someuser at some_emplacement as flatpages %}
        {% get_customflatpages '/about/' for someuser at some_emplacement as about_pages %}
    """
    bits = token.split_contents()
    syntax_message = ("%(tag_name)s expects a syntax of %(tag_name)s "
                      "['url_starts_with'] [for user] [at emplacement] as context_name" %
                      dict(tag_name=bits[0]))
    # Must have at 3-6 bits in the tag
    if len(bits) >= 3 and len(bits) <= 8:

        # If there's an even number of bits, there's no prefix
        if len(bits) % 2 == 0:
            prefix = bits[1]
        else:
            prefix = None

        # The very last bit must be the context name
        if bits[-2] != 'as':
            raise template.TemplateSyntaxError(syntax_message)
        context_name = bits[-1]

        user = None
        emplacement = None

        # If there are 7 or 8 bits, there is a user and an emplacement defined
        if len(bits) >= 7:
            if bits[-4] != 'at':
                raise template.TemplateSyntaxError(syntax_message)
            emplacement = bits[-3]
            if bits[-6] != 'for':
                raise template.TemplateSyntaxError(syntax_message)
            user = bits[-5]

        # If there are 5 or 6 bits, there is a user or an emplacement defined
        elif len(bits) >= 5:
            if bits[-4] == 'for':
                user = bits[-3]
            elif bits[-4] == 'at':
                emplacement = bits[-3]
            else:
                raise template.TemplateSyntaxError(syntax_message)

        return CustomFlatpageNode(context_name, starts_with=prefix, user=user, emplacement=emplacement)
    else:
        raise template.TemplateSyntaxError(syntax_message)

