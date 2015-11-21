# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capoeira', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corda',
            name='id',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='turma',
            name='id',
        ),
        migrations.AlterField(
            model_name='corda',
            name='cor',
            field=models.CharField(primary_key=True, max_length=100, serialize=False),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='nome',
            field=models.CharField(primary_key=True, max_length=100, serialize=False),
        ),
        migrations.AlterField(
            model_name='turma',
            name='nome',
            field=models.CharField(primary_key=True, max_length=100, serialize=False),
        ),
    ]
