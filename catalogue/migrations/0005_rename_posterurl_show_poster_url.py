# Generated by Django 5.0.2 on 2024-03-19 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_show'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='posterUrl',
            new_name='poster_url',
        ),
    ]