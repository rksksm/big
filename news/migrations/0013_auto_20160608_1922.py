# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20160608_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='gist',
            new_name='intro_text',
        ),
        migrations.RenameField(
            model_name='slide',
            old_name='image_name',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='heading',
            name='text',
        ),
        migrations.AddField(
            model_name='slide',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]