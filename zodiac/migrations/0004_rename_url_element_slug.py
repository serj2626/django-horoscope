# Generated by Django 3.2.13 on 2023-06-16 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zodiac', '0003_alter_zodiac_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='element',
            old_name='url',
            new_name='slug',
        ),
    ]
