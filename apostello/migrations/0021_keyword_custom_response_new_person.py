# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 14:58
from __future__ import unicode_literals

import apostello.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apostello', '0020_auto_20171116_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='custom_response_new_person',
            field=models.CharField(blank=True, help_text='This text will be sent back as a reply when any incoming message matches this keyword and the contact is new. If empty, the normal custom response will be used.', max_length=100, validators=[django.core.validators.RegexValidator('^[\\s\\w@?£!1$"¥#è?¤é%ù&ì\\ò(Ç)*:Ø+;ÄäøÆ,<LÖlöæ\\-=ÑñÅß.>ÜüåÉ/§à¡¿\']+$', message='You can only use GSM characters.'), apostello.validators.less_than_sms_char_limit], verbose_name='Auto response used when the contact is new'),
        ),
    ]
