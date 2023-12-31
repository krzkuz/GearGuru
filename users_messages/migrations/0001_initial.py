# Generated by Django 4.2.2 on 2023-07-03 22:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gear', '0012_remove_guitar_images_image_guitar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='message_from', to=settings.AUTH_USER_MODEL)),
                ('images', models.ManyToManyField(blank=True, to='gear.image')),
                ('related_gear', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gear.guitar')),
                ('to_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='message_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
