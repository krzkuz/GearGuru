# Generated by Django 4.2.2 on 2023-07-03 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_customuser_apartment_alter_customuser_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='average_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
    ]
