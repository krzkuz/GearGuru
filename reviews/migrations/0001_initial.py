# Generated by Django 4.2.2 on 2023-07-03 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(choices=[('5', 'Five stars'), ('4', 'Four stars'), ('3', 'Three stars'), ('2', 'Two stars'), ('1', 'One star')], max_length=1)),
                ('description', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
