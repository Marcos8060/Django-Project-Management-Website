# Generated by Django 4.0.3 on 2022-03-15 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prohub', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='user',
            new_name='owner',
        ),
    ]
