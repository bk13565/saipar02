# Generated by Django 3.2.7 on 2022-02-07 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0014_auto_20220207_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='link',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='openingmodel',
            name='link',
            field=models.URLField(max_length=300),
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='link',
            field=models.URLField(max_length=300),
        ),
    ]
