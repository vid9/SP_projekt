# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 15:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poraba', '0006_auto_20170115_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specifikacije',
            old_name='dolžina',
            new_name='dolzina',
        ),
        migrations.RenameField(
            model_name='specifikacije',
            old_name='višina',
            new_name='visina',
        ),
    ]
