# Generated by Django 3.2.7 on 2022-01-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0012_alter_projectmodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='upload_link',
            field=models.FileField(blank=True, upload_to='static/'),
        ),
    ]
