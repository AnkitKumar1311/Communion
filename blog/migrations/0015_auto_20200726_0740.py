# Generated by Django 3.0.8 on 2020-07-26 02:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200726_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 26, 2, 10, 12, 702671, tzinfo=utc)),
        ),
    ]
