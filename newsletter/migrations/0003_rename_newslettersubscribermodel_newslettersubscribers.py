# Generated by Django 3.2.7 on 2021-10-15 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20211015_2323'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsletterSubscriberModel',
            new_name='NewsletterSubscribers',
        ),
    ]
