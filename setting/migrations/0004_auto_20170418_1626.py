# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 08:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0003_welcomesystemmessage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='welcomesystemmessage',
            options={'verbose_name': '初始化系统消息', 'verbose_name_plural': '初始化系统消息'},
        ),
    ]