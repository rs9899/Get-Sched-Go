# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timetable', '0015_auto_20171008_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='DeadLineTime',
            field=models.TimeField(default='23:30:00', null=True),
        ),
    ]
