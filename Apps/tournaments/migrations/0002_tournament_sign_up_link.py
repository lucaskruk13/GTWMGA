# Generated by Django 2.0.1 on 2018-01-13 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='sign_up_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
