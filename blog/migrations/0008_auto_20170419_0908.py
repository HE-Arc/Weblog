# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170419_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
