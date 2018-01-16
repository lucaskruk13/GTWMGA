# Generated by Django 2.0.1 on 2018-01-12 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfer', '0002_auto_20180112_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='golfer',
            name='board_member',
            field=models.IntegerField(choices=[(0, 'Non Board Member'), (1, 'Board Member'), (2, 'Treasurer'), (3, 'Tournament Chairman'), (4, 'Secretary'), (5, 'Website Admin'), (6, 'Handicap Chairman'), (7, 'Vice President'), (8, 'President')], default=0),
        ),
    ]
