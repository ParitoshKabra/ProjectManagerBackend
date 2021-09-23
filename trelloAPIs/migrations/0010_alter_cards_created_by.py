# Generated by Django 3.2.6 on 2021-09-07 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trelloAPIs', '0009_alter_users_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trelloAPIs.Cards.created_by+', to=settings.AUTH_USER_MODEL),
        ),
    ]
