# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capoeira', '0002_auto_20151124_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fabrica',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Flyweight',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='GerarRelatorio',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
            ],
        ),
    ]
