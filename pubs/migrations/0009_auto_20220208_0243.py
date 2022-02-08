# Generated by Django 3.2.7 on 2022-02-08 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubs', '0008_rename_ocasionalpapermodel_occasionalpapermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussionpapersmodel',
            name='paper_link',
            field=models.FileField(blank=True, upload_to='pubs/discussion_papers'),
        ),
        migrations.AlterField(
            model_name='occasionalpapermodel',
            name='paper_link',
            field=models.FileField(blank=True, upload_to='pubs/occassional_papers'),
        ),
        migrations.AlterField(
            model_name='reportsmodel',
            name='paper_link',
            field=models.FileField(blank=True, upload_to='pubs/reports_and_policy_briefs'),
        ),
        migrations.AlterField(
            model_name='saiparbookshelfmodel',
            name='link',
            field=models.FileField(blank=True, upload_to='pubs/SAIPAR_bookshelf'),
        ),
        migrations.AlterField(
            model_name='zssjmodel',
            name='link',
            field=models.FileField(blank=True, upload_to='pubs/zssj'),
        ),
    ]