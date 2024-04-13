# Generated by Django 5.0.2 on 2024-04-13 01:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
        ('user', '0006_alter_user_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='likes',
        ),
        migrations.AddField(
            model_name='user',
            name='likes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.genre'),
        ),
    ]