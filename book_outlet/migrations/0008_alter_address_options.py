# Generated by Django 4.2.4 on 2023-09-07 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0007_address_author_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Address Entries'},
        ),
    ]