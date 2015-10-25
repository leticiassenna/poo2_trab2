# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('complemento', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField()),
                ('mestre_examinador', models.CharField(max_length=100)),
                ('endereco', models.ForeignKey(to='capoeira.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sequencia_corda', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.ForeignKey(to='capoeira.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('rg', models.CharField(max_length=20)),
                ('data_nascimento', models.DateField()),
                ('telefone', models.CharField(max_length=50)),
                ('profissao', models.CharField(max_length=50)),
                ('grau_escolar', models.CharField(max_length=50)),
                ('cor_corda', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('turno', models.CharField(max_length=100)),
                ('horario', models.DateField()),
                ('dia_semana', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='capoeira.Pessoa')),
                ('pai', models.CharField(max_length=100)),
                ('mae', models.CharField(max_length=100)),
            ],
            bases=('capoeira.pessoa',),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='capoeira.Pessoa')),
                ('registro', models.CharField(max_length=100)),
            ],
            bases=('capoeira.pessoa',),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='endereco',
            field=models.ForeignKey(to='capoeira.Endereco'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='grupo',
            field=models.ForeignKey(to='capoeira.Grupo'),
        ),
        migrations.AddField(
            model_name='exame',
            name='turma',
            field=models.ForeignKey(to='capoeira.Turma'),
        ),
        migrations.AddField(
            model_name='turma',
            name='aluno',
            field=models.ForeignKey(to='capoeira.Aluno'),
        ),
        migrations.AddField(
            model_name='turma',
            name='professor',
            field=models.ForeignKey(to='capoeira.Professor'),
        ),
    ]
