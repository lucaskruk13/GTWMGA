# Generated by Django 2.0.1 on 2018-01-15 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0009_auto_20180115_0729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='points',
            old_name='participation_points',
            new_name='points',
        ),
        migrations.RemoveField(
            model_name='points',
            name='extra_points',
        ),
    ]
