# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-21 17:58
from __future__ import unicode_literals

import blogosphere.mixins.models.image
from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20180514_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, height_field='height', help_text='Usado para ilustración.', max_length=255, upload_to=blogosphere.mixins.models.image.image_upload_to_dispatcher, verbose_name='imagen del blog', width_field='width'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='banner_image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, height_field='banner_height', help_text='Usado para ilustración.', max_length=255, upload_to=blogosphere.mixins.models.image.image_upload_to_dispatcher, verbose_name='banner del blog', width_field='banner_width'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, height_field='height', help_text='Usado para ilustración.', max_length=255, upload_to=blogosphere.mixins.models.image.image_upload_to_dispatcher, verbose_name='imagen del blog', width_field='width'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, height_field='height', help_text='Usado para ilustración.', max_length=255, upload_to=blogosphere.mixins.models.image.image_upload_to_dispatcher, verbose_name='imagen del blog', width_field='width'),
        ),
    ]
