# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frame', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content1model',
            name='slug',
            field=models.SlugField(default=1, help_text='A label for the publication config', max_length=31, unique=True),
            preserve_default=False,
        ),
    ]
