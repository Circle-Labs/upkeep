# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-22 02:55
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0003_auto_20160410_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Betas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(regex='^(\\+\\d{1,2}\\s)?\\(?\\d{3}\\)?[\\s.-]?\\d{3}[\\s.-]?\\d{4}$')]),
        ),
    ]
