# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 12:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0024_remove_section_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breaking',
            name='priority',
        ),
    ]
