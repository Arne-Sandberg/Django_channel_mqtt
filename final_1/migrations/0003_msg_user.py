# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('final_1', '0002_auto_20171111_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg',
            name='user',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
