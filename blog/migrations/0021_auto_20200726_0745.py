# Generated by Django 3.0.8 on 2020-07-26 02:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20200726_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 26, 2, 15, 39, 135694, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug_title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
