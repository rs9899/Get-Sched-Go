# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 18:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timetable', '0010_auto_20171007_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='StartTime',
            field=models.TimeField(default=datetime.date.today, null=True),
        ),
    ]
