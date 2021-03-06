# Generated by Django 4.0.3 on 2022-03-15 11:59

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
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200, null=True)),
                ('project_image', models.ImageField(blank=True, upload_to='image')),
                ('description', models.TextField()),
                ('project_url', models.URLField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('profile_image', models.ImageField(blank=True, upload_to='image')),
                ('bio', models.TextField(blank=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.project')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='image')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=2000)),
                ('likes', models.IntegerField(default=0)),
                ('comment', models.TextField(blank=True)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
