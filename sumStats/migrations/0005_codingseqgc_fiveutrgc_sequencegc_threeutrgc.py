# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sumStats', '0004_codingseqlength_fiveutrlength_threeutrlength'),
    ]

    operations = [
        migrations.CreateModel(
            name='codingSeqGC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seqName', models.CharField(max_length=200)),
                ('seqLen', models.FloatField(default=None)),
                ('genotype', models.ForeignKey(to='sumStats.Genotype')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='fiveUTRgc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seqName', models.CharField(max_length=200)),
                ('seqLen', models.FloatField(default=None)),
                ('genotype', models.ForeignKey(to='sumStats.Genotype')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='sequenceGC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seqName', models.CharField(max_length=200)),
                ('seqLen', models.FloatField(default=None)),
                ('genotype', models.ForeignKey(to='sumStats.Genotype')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='threeUTRgc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seqName', models.CharField(max_length=200)),
                ('seqLen', models.FloatField(default=None)),
                ('genotype', models.ForeignKey(to='sumStats.Genotype')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
