# Generated by Django 2.0.1 on 2018-01-16 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0014_auto_20180116_0445'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='points',
            options={'ordering': ('gross_or_net', 'golfer')},
        ),
    ]
