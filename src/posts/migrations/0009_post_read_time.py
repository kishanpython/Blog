# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-17 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20181017_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='read_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
