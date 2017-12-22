# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-21 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_management', '0003_itemmapper'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemmapper',
            name='_name',
        ),
        migrations.RemoveField(
            model_name='itemmapper',
            name='_notes',
        ),
        migrations.AddField(
            model_name='itemmapper',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='itemmapper',
            name='notes',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
