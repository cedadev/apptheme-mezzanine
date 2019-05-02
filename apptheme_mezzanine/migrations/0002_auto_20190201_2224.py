# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-02-01 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptheme_mezzanine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='content',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='leader',
            field=models.CharField(blank=True, help_text=b'Optional brief intro. Not rendered in default template.', max_length=4096),
        ),
    ]
