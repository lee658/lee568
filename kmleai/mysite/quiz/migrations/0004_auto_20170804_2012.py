# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quiz_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='quiz',
            name='image_1',
            field=models.ImageField(default='', upload_to='quiz/quiz/%Y/%m/%d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='image_2',
            field=models.ImageField(default='', upload_to='quiz/quiz/%Y/%m/%d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='image_3',
            field=models.ImageField(default='', upload_to='quiz/quiz/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
