# Generated by Django 3.0.8 on 2020-07-26 02:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20200726_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='relation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 26, 7, 39, 14, 532766)),
        ),
    ]
