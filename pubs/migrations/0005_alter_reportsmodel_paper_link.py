# Generated by Django 3.2.7 on 2022-01-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubs', '0004_alter_saiparbookshelfmodel_book_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportsmodel',
            name='paper_link',
            field=models.FileField(blank=True, upload_to='static/publications/reports_and_policy_briefs'),
        ),
    ]
