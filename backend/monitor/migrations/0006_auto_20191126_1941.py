# Generated by Django 2.2.7 on 2019-11-26 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0005_repository_owner_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repository',
            old_name='owner_username',
            new_name='owner_avatar_url',
        ),
        migrations.RemoveField(
            model_name='repository',
            name='owner',
        ),
        migrations.AddField(
            model_name='repository',
            name='owner_login',
            field=models.CharField(default='davidpierre21', max_length=255),
            preserve_default=False,
        ),
    ]
