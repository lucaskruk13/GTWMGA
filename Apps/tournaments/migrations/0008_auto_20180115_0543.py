# Generated by Django 2.0.1 on 2018-01-15 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0007_points_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='points',
            name='gross_or_net',
            field=models.CharField(choices=[('G', 'Gross'), ('N', 'Net')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='points',
            name='place_finished',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
