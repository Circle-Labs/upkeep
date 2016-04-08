# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('nextReminder', models.DateTimeField()),
                ('frequency', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('smsVerifyCode', models.IntegerField(blank=True)),
                ('contacts', models.ManyToManyField(blank=True, to='reminders.Contact')),
            ],
        ),
    ]
