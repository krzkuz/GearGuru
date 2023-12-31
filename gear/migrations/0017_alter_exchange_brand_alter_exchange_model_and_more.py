# Generated by Django 4.2.2 on 2023-07-12 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0016_exchange_title_rent_title_sell_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='brand',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='model',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rent',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rent',
            name='renting_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Renting time in days'),
        ),
    ]
