# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170313_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(verbose_name=True),
        ),
    ]