# Generated by Django 4.2.1 on 2023-06-09 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_openinghours_openinghours_day_hour_unique'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OpeningHours',
            new_name='OpeningHour',
        ),
    ]