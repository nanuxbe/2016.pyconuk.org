# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyconuk', '0006_auto_20160826_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='show_sponsors',
            field=models.BooleanField(default=True),
        ),
    ]
