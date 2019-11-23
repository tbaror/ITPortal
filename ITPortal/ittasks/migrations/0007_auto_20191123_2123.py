# Generated by Django 2.2.7 on 2019-11-23 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ittasks', '0006_auto_20191123_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childtask',
            name='task_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 23, 21, 23, 41, 570000)),
        ),
        migrations.AlterField(
            model_name='childtask',
            name='task_due_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 23, 21, 23, 41, 570000)),
        ),
        migrations.AlterField(
            model_name='childtask',
            name='task_updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 23, 21, 23, 41, 570000)),
        ),
        migrations.AlterField(
            model_name='maintask',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 23, 21, 23, 41, 570000)),
        ),
        migrations.AlterField(
            model_name='maintask',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 23, 21, 23, 41, 570000)),
        ),
        migrations.AlterField(
            model_name='maintask',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 23, 21, 23, 41, 570000)),
        ),
    ]
