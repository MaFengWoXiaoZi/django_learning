# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-30 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20180123_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=5),
        ),
    ]