# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-16 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adminbroadcast',
            options={'verbose_name': '管理广播', 'verbose_name_plural': '管理广播'},
        ),
        migrations.AlterField(
            model_name='adminbroadcast',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
