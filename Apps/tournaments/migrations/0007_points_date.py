# Generated by Django 2.0.1 on 2018-01-13 04:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0006_auto_20180113_0440'),
    ]

    operations = [
        migrations.AddField(
            model_name='points',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]