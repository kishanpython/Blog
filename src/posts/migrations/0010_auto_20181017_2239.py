# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-17 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_post_read_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='read_time',
            field=models.IntegerField(default=0),
        ),
    ]
