# Generated by Django 4.1.2 on 2022-12-22 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_products_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]
