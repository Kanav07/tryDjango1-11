# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-25 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_restaurantlocation_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
