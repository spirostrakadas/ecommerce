# Generated by Django 4.1.2 on 2022-12-08 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_user_name'),
        ('products', '0004_rename_tittle_products_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
