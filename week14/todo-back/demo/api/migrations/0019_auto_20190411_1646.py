# Generated by Django 2.2 on 2019-04-11 10:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20190411_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 11, 16, 46, 17, 94381)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 13, 16, 46, 17, 94381)),
        ),
    ]
