# Generated by Django 4.0.1 on 2022-01-04 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_active',
            new_name='in_active',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='is_stock',
            new_name='in_stock',
        ),
    ]
