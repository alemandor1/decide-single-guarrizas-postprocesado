# Generated by Django 2.0 on 2018-02-16 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mixnet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mixnet',
            old_name='vote_id',
            new_name='voting_id',
        ),
    ]
