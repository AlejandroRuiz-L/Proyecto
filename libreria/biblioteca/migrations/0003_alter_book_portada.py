# Generated by Django 5.0.2 on 2024-04-14 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_book_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='portada',
            field=models.ImageField(blank=True, default=None, upload_to=''),
        ),
    ]
