# Generated by Django 3.0.8 on 2020-07-23 22:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200724_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 23, 22, 17, 56, 639411, tzinfo=utc)),
        ),
    ]