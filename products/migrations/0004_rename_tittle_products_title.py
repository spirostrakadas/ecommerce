# Generated by Django 4.1.2 on 2022-12-07 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_featured_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='tittle',
            new_name='title',
        ),
    ]