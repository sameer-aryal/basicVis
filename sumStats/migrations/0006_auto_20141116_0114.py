# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sumStats', '0005_codingseqgc_fiveutrgc_sequencegc_threeutrgc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codingseqlength',
            name='seqLen',
            field=models.FloatField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fiveutrlength',
            name='seqLen',
            field=models.FloatField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencelength',
            name='seqLen',
            field=models.FloatField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='threeutrlength',
            name='seqLen',
            field=models.FloatField(default=None),
            preserve_default=True,
        ),
    ]
