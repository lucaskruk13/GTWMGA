# Generated by Django 2.0.1 on 2018-01-16 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0013_auto_20180115_2053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='points',
            options={'ordering': ('golfer',)},
        ),
        migrations.AlterField(
            model_name='tournament',
            name='course',
            field=models.CharField(choices=[('OAKS', 'The Oaks'), ('PT', 'Panther Trail'), ('LW', 'Lake Windcrest')], default='OAKS', max_length=4),
        ),
    ]