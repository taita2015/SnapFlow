# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 01:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20170419_0920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertousermessage',
            old_name='user',
            new_name='a_user',
        ),
        migrations.RenameField(
            model_name='usertousermessage',
            old_name='to_user',
            new_name='b_user',
        ),
    ]
