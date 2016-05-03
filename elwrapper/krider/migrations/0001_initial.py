# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-03 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('year', models.IntegerField()),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
