# Generated by Django 4.1.7 on 2023-03-14 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='date_update',
            new_name='update_at',
        ),
    ]