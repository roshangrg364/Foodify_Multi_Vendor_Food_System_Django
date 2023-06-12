# Generated by Django 4.2.1 on 2023-06-10 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0006_rename_openinghours_openinghour'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='openinghour',
            name='day_hour_unique',
        ),
        migrations.AddConstraint(
            model_name='openinghour',
            constraint=models.UniqueConstraint(fields=('vendor', 'day', 'from_hour', 'to_hour'), name='day_hour_unique'),
        ),
    ]