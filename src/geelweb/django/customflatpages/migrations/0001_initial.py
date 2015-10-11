# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomFlatPage',
            fields=[
                ('flatpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='flatpages.FlatPage')),
                ('emplacement', models.CharField(default=b'footer', max_length=12, choices=[(b'footer', b'Flatpage with link in footer'), (b'menu', b'Flatpage with link in menu')])),
                ('order', models.IntegerField(default=0)),
            ],
            bases=('flatpages.flatpage',),
        ),
    ]
