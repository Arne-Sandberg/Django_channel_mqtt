# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('par1', models.IntegerField()),
                ('par2', models.IntegerField()),
                ('par3', models.IntegerField()),
                ('par4', models.FloatField()),
                ('par5', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=20)),
                ('payload', models.CharField(max_length=200)),
                ('qos', models.SmallIntegerField()),
                ('host', models.GenericIPAddressField()),
                ('port', models.IntegerField()),
            ],
        ),
    ]
