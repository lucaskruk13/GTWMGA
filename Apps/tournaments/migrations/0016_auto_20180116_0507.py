# Generated by Django 2.0.1 on 2018-01-16 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0015_auto_20180116_0506'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='points',
            options={'ordering': ('golfer',)},
        ),
    ]
