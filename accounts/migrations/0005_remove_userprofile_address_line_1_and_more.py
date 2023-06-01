# Generated by Django 4.2.1 on 2023-06-01 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_latitude_userprofile_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address_line_1',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='address_line_2',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]