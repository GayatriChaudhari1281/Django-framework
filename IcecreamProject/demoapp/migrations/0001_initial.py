# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-06-03 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Icecream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavour', models.CharField(max_length=15)),
                ('ingrediants', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('expdate', models.DateField()),
            ],
        ),
    ]
