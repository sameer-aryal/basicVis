# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genotype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genotype_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SequenceLength',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seqLen', models.DecimalField(max_digits=19, decimal_places=4)),
                ('genotype', models.ForeignKey(to='sumStats.Genotype')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
