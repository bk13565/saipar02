# Generated by Django 3.2.7 on 2021-10-19 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20211019_1237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='iab',
            new_name='International_Advisory_Board',
        ),
    ]
