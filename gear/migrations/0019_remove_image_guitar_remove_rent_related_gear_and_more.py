# Generated by Django 4.2.2 on 2023-07-12 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0018_alter_guitar_bridge_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='guitar',
        ),
        migrations.RemoveField(
            model_name='rent',
            name='related_gear',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='related_gear',
        ),
        migrations.DeleteModel(
            name='Exchange',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Rent',
        ),
        migrations.DeleteModel(
            name='Sell',
        ),
    ]
