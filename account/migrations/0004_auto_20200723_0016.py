# Generated by Django 3.0.8 on 2020-07-22 18:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_follower'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='show_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='follower',
            name='relation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 23, 0, 16, 49, 55236)),
        ),
    ]