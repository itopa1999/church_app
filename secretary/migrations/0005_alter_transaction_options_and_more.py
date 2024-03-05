# Generated by Django 4.2.7 on 2024-03-05 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretary', '0004_church_member_address_church_member_age_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveIndex(
            model_name='transaction',
            name='secretary_t_date_a550f2_idx',
        ),
        migrations.AddIndex(
            model_name='transaction',
            index=models.Index(fields=['-date'], name='secretary_t_date_f22cbc_idx'),
        ),
    ]
