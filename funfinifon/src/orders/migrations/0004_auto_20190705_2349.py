# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-07-05 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190705_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
