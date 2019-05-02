# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-02-07 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptheme_mezzanine', '0003_auto_20190205_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='content',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='leader',
            field=models.CharField(blank=True, help_text=b'Optional brief intro.', max_length=4096),
        ),
    ]
