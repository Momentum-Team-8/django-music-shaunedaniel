# Generated by Django 3.2.4 on 2021-06-21 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_alter_album_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='created_at',
            new_name='album_art',
        ),
    ]
