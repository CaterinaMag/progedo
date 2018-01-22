# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-09 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='slug',
            field=models.SlugField(default=None, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
