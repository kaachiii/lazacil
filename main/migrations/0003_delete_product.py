# Generated by Django 5.1.1 on 2024-09-15 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_delete_moodentry'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]