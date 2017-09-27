# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0006_auto_20170926_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailySched',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Active_day', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('UserProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Slots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartTime', models.DateTimeField()),
                ('EndTime', models.DateTimeField()),
                ('SlotNum', models.IntegerField()),
                ('Day_Sched', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Timetable.DailySched')),
                ('UserProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]