# Generated by Django 4.0.3 on 2022-03-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nft_Api', '0011_remove_user_collected_user_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='properties',
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]