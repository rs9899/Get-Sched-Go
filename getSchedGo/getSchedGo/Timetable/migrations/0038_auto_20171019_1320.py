# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 07:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timetable', '0037_auto_20171018_0517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructorassignment',
            name='StudentData',
        ),
        migrations.RemoveField(
            model_name='instructorexam',
            name='StudentData',
        ),
        migrations.AlterField(
            model_name='event',
            name='DeadLineDate',
            field=models.DateField(blank=True, default=datetime.date(2017, 10, 22), null=True),
        ),
        migrations.AlterField(
            model_name='instructorassignment',
            name='DeadLineDate',
            field=models.DateField(blank=True, default=datetime.date(2017, 10, 22), null=True),
        ),
    ]
