# Generated by Django 4.2.2 on 2023-07-02 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_customuser_apartment_alter_customuser_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='apartment',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='street',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='zip_code',
            field=models.CharField(max_length=50, null=True),
        ),
    ]