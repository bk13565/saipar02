# Generated by Django 3.2.7 on 2022-01-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upload',
            field=models.FileField(blank=True, upload_to='static/blog'),
        ),
    ]
