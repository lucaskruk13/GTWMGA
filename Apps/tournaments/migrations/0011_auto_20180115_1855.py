# Generated by Django 2.0.1 on 2018-01-15 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0010_auto_20180115_0802'),
    ]

    operations = [
        migrations.RenameField(
            model_name='points',
            old_name='points',
            new_name='participation_points',
        ),
        migrations.AddField(
            model_name='points',
            name='extra_Points',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]