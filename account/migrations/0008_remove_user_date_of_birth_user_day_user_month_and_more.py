# Generated by Django 4.1.5 on 2023-03-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='user',
            name='day',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='month',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]
