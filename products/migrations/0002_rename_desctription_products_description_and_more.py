# Generated by Django 4.1.2 on 2022-12-01 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='desctription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='title',
            new_name='tittle',
        ),
    ]
