# Generated by Django 5.0.4 on 2024-11-12 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Quantity',
            new_name='quantity',
        ),
    ]
