# Generated by Django 2.0.1 on 2018-01-12 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfer', '0005_golfer_board_member_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golfer',
            name='board_member_photo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]