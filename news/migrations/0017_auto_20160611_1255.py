# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 07:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_card_section'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='section',
            new_name='heading',
        ),
    ]
