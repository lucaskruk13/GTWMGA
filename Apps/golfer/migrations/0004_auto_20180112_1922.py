# Generated by Django 2.0.1 on 2018-01-12 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfer', '0003_golfer_board_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golfer',
            name='handicap',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
    ]
