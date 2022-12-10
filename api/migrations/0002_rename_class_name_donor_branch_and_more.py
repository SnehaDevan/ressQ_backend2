# Generated by Django 4.1.4 on 2022-12-10 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donor',
            old_name='class_name',
            new_name='branch',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='first_name',
        ),
        migrations.AlterField(
            model_name='newuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
