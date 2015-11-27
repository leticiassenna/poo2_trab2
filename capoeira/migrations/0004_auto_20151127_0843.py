# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capoeira', '0003_fabrica_flyweight_gerarrelatorio'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GerarRelatorio',
            new_name='Relatorio',
        ),
    ]
