# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomFlatPage',
            fields=[
                ('flatpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='flatpages.FlatPage')),
                ('emplacement', models.CharField(default=b'footer', max_length=12, choices=[(b'footer', b'Footer')])),
                ('order', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=('flatpages.flatpage',),
        ),
    ]
