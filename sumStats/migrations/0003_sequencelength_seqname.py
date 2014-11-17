# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sumStats', '0002_auto_20141105_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='sequencelength',
            name='seqName',
            field=models.CharField(default='Sameer', max_length=200),
            preserve_default=False,
        ),
    ]
