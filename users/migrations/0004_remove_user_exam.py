# Generated by Django 4.2.7 on 2024-02-21 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_district_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='exam',
        ),
    ]
