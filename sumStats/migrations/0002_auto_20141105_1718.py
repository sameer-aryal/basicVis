# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sumStats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequencelength',
            name='seqLen',
            field=models.IntegerField(default=None),
            preserve_default=True,
        ),
    ]
