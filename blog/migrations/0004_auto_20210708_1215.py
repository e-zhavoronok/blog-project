# Generated by Django 3.2 on 2021-07-08 09:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210708_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 8, 9, 15, 17, 16382, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 8, 9, 15, 17, 12380, tzinfo=utc)),
        ),
    ]
