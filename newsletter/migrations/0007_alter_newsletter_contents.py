# Generated by Django 3.2.7 on 2022-02-08 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_auto_20220207_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='contents',
            field=models.FileField(upload_to='newsletter/saipar_newsletters'),
        ),
    ]
