# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timetable', '0008_auto_20171007_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='EndDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
