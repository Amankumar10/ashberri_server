# Generated by Django 4.1.5 on 2023-04-21 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='picture',
        ),
    ]
