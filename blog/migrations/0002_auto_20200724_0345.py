# Generated by Django 3.0.8 on 2020-07-23 22:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 23, 22, 15, 32, 276119, tzinfo=utc)),
        ),
    ]
