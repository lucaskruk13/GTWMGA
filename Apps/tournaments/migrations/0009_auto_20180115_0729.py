# Generated by Django 2.0.1 on 2018-01-15 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0008_auto_20180115_0543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='points',
            name='participation',
        ),
        migrations.AddField(
            model_name='points',
            name='participation_points',
            field=models.IntegerField(default=100),
        ),
    ]
