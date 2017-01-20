# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 22:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poraba', '0008_auto_20170115_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poraba', models.DecimalField(decimal_places=2, max_digits=4)),
                ('ime', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='poraba.Car')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='specifikacije',
            name='poraba',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]