# Generated by Django 3.2.6 on 2021-09-09 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trelloAPIs', '0015_projects_admins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_tym',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
