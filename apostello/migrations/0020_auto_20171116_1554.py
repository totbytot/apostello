# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apostello', '0019_remove_smsinbound_matched_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipient',
            name='notes',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='can_see_contact_notes',
            field=models.BooleanField(default=False),
        ),
    ]
