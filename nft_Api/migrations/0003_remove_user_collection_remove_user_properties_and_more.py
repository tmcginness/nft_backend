# Generated by Django 4.0.3 on 2022-03-17 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nft_Api', '0002_alter_nft_properties'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='user',
            name='properties',
        ),
        migrations.AddField(
            model_name='nft',
            name='blockchain',
            field=models.CharField(default='Ethereum', max_length=16),
        ),
        migrations.AddField(
            model_name='nft',
            name='collection',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='nft',
            name='offer_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='nft',
            name='owner',
            field=models.CharField(default='None', max_length=64),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='collected',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='created',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='favorited',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nft',
            name='properties',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='offers',
            field=models.TextField(blank=True, null=True),
        ),
    ]