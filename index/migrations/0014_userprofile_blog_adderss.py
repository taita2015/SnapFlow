# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-04 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_userprofile_work_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='blog_adderss',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]