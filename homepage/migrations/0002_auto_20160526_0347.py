# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='year_in_school',
            field=models.IntegerField(choices=[(1, '1ro'), (2, '2do'), (3, '3ro'), (4, '4to'), (5, '5to')], default=1),
        ),
    ]
