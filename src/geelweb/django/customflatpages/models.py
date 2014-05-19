from django.db import models
from django.contrib.sites.models import Site
from django.conf import settings
from django.contrib.flatpages.models import FlatPage

class CustomFlatPage(FlatPage):
    emplacement = models.CharField(max_length=12,
            choices=settings.FLATPAGES_EMPLACEMENTS,
            default=settings.FLATPAGES_DEFAULT_EMPLACEMENT)
    order = models.IntegerField(default=0)

    def save(self):
        super(CustomFlatPage, self).save()
        self.sites = [Site.objects.get(pk=settings.SITE_ID)]
        super(CustomFlatPage, self).save()
