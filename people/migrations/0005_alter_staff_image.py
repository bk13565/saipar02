# Generated by Django 3.2.7 on 2021-10-22 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_alter_researchstaff_research_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/people'),
        ),
    ]
