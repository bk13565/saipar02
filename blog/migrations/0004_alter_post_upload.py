# Generated by Django 3.2.7 on 2022-02-04 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload',
            field=models.FileField(blank=True, upload_to='blog'),
        ),
    ]
