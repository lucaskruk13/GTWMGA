# Generated by Django 2.0.1 on 2018-01-22 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0020_auto_20180122_2128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interclub',
            options={'ordering': ('date',)},
        ),
        migrations.RemoveField(
            model_name='interclub',
            name='breakStart',
        ),
    ]