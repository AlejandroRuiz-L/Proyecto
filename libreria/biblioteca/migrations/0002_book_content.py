# Generated by Django 5.0.2 on 2024-04-14 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='content',
            field=models.BinaryField(blank=True),
        ),
    ]