# Generated by Django 4.2.2 on 2023-07-01 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_guitar_alter_customuser_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='guitar',
        ),
    ]
