# Generated by Django 2.2.7 on 2019-11-24 16:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='users',
            field=models.ManyToManyField(related_name='watched_repositories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='author',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
