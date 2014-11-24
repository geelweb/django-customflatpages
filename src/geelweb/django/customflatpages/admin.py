from django.contrib import admin
from django import forms
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models

from geelweb.django.customflatpages.models import CustomFlatPage

class CustomFlatPageForm(FlatpageForm):
    class Meta:
        model = CustomFlatPage
        exclude = []

class CustomFlatPageAdmin(FlatPageAdmin):
    form = CustomFlatPageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'emplacement', 'order')}),
    )
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    list_display = ('url', 'title', 'emplacement', 'order', )
    list_filter = ('emplacement', )

    class Media:
        js = ('ckeditor/ckeditor.js',)

admin.site.unregister(FlatPage)
admin.site.register(CustomFlatPage, CustomFlatPageAdmin)
