# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-06-23 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('rollno', models.IntegerField()),
                ('marks', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
