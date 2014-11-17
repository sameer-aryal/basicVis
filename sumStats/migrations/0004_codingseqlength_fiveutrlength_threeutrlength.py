# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sumStats', '0003_sequencelength_seqname'),
    ]

    operations = [
        migrations.CreateModel(
            name='codingSeqLength',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seqName', models.CharField(max_length=200)),
                ('seqLen', models.IntegerField(default=None)),
                ('genotype', models.ForeignKey(to='sumStats.Genotype')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='fiveUTRlength',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seqName', models.CharField(max_length=200)),
                ('seqLen', models.IntegerField(default=None)),
                ('genotype', models.ForeignKey(to='sumStats.Genotype')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='threeUTRlength',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seqName', models.CharField(max_length=200)),
                ('seqLen', models.IntegerField(default=None)),
                ('genotype', models.ForeignKey(to='sumStats.Genotype')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
