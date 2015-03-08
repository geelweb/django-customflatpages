# -*- coding: utf-8 -*-

from django.test import TestCase
from django.utils import unittest
from django.conf import settings
from django.contrib.sites.models import Site
from django.template import Context, Template
from geelweb.django.customflatpages.models import CustomFlatPage

class CustomFlatPageTestCase(unittest.TestCase):
    def test_default_emplacement(self):
        p = CustomFlatPage(title="Café!", url='/cafe/')
        self.assertEqual(
            p.emplacement,
            settings.FLATPAGES_DEFAULT_EMPLACEMENT)

class FlatpageTemplateTagTests(TestCase):
    def setUp(self):
        self.site1 = Site(pk=1, domain='example.com', name='example.com')
        self.site1.save()

        self.fp1 = CustomFlatPage.objects.create(
            url='/flatpage/', title='A Flatpage', content="Isn't it flat!",
            enable_comments=False, template_name='', registration_required=False,
            emplacement='footer', order=2
        )
        self.fp2 = CustomFlatPage.objects.create(
            url='/location/flatpage/', title='A Nested Flatpage', content="Isn't it flat and deep!",
            enable_comments=False, template_name='', registration_required=False,
            emplacement='footer', order=1
        )
        self.fp3 = CustomFlatPage.objects.create(
            url='/sekrit/', title='Sekrit Flatpage', content="Isn't it sekrit!",
            enable_comments=False, template_name='', registration_required=False,
            emplacement='menu'
        )

        #self.fp1.sites.add(self.site1)
        #self.fp2.sites.add(self.site1)
        #self.fp3.sites.add(self.site1)

    def test_get_customflatpages_tag(self):
        out = Template(
            "{% load customflatpages %}"
            "{% get_customflatpages at 'menu' as flatpages_menu %}"
            "{% for page in flatpages_menu %}"
            "{{ page.title }},"
            "{% endfor %}"
        ).render(Context())
        self.assertEqual(out, "Sekrit Flatpage,")

        out = Template(
            "{% load customflatpages %}"
            "{% get_customflatpages at 'footer' as flatpages %}"
            "{% for page in flatpages %}"
            "{{ page.title }},"
            "{% endfor %}"
        ).render(Context())
        self.assertEqual(out, "A Nested Flatpage,A Flatpage,")
