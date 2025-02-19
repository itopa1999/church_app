# Generated by Django 4.2.7 on 2024-02-20 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Department',
            new_name='District',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-district']},
        ),
        migrations.RemoveIndex(
            model_name='user',
            name='users_user_departm_b77304_idx',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='department',
            new_name='district',
        ),
        migrations.RenameIndex(
            model_name='district',
            new_name='users_distr_name_4b2276_idx',
            old_name='users_depar_name_30ebb2_idx',
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['-district'], name='users_user_distric_1a3a17_idx'),
        ),
    ]
