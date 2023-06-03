# Generated by Django 4.1.5 on 2023-06-02 12:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_alter_user_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friend_requests',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
