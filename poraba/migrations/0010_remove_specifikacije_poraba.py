# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 00:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poraba', '0009_auto_20170115_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specifikacije',
            name='poraba',
        ),
    ]
