# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2018-01-15 12:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20180114_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
    ]
