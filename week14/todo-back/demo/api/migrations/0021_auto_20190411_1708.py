# Generated by Django 2.2 on 2019-04-11 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20190411_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 11, 17, 8, 39, 187037)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 13, 17, 8, 39, 187037)),
        ),
    ]