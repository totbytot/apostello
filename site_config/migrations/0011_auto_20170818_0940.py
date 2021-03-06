# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("site_config", "0010_auto_20170706_1444")]

    operations = [
        migrations.AlterField(
            model_name="siteconfiguration",
            name="sms_rolling_expiration_days",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="The number of days a message will be kept by apostello before being deleted. If blank, then messages will be kept forever.",
                null=True,
                verbose_name="Rolling SMS Expiration",
            ),
        )
    ]
