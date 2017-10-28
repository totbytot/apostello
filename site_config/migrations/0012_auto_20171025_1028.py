# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('site_config', '0011_auto_20170818_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='twilio_account_sid',
            field=models.CharField(blank=True, help_text='Your Twilio Account SID. See https://support.twilio.com/hc/en-us/articles/223136607-What-is-an-Application-SID-', max_length=34, null=True, verbose_name='Twilio Account SID'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='twilio_auth_token',
            field=models.CharField(blank=True, help_text='Your Twilio Auth Token. See https://support.twilio.com/hc/en-us/articles/223136027-Auth-Tokens-and-how-to-change-them', max_length=32, null=True, verbose_name='Twilio Auth Token'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='twilio_from_num',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Your Twilio Number. This is the number we will send messages from.', max_length=128, null=True, verbose_name='Twilio Phone Number'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='twilio_sending_cost',
            field=models.DecimalField(blank=True, decimal_places=4, help_text='The cost of sending an SMS. You can find this here: https://www.twilio.com/sms/pricing', max_digits=5, null=True, verbose_name='Twilio Sending Cost'),
        ),
    ]
