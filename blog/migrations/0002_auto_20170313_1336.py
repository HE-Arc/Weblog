# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(verbose_name=True),
        ),
    ]
