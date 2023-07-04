# Generated by Django 4.2.2 on 2023-07-02 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0008_exchange'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guitar',
            name='price',
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('more_info', models.TextField(verbose_name='More informations')),
                ('related_gear', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gear.guitar')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('renting_time', models.IntegerField(verbose_name='Renting time in days')),
                ('more_info', models.TextField(verbose_name='More informations')),
                ('related_gear', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gear.guitar')),
            ],
        ),
    ]