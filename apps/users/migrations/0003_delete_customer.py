# Generated by Django 4.1.7 on 2023-12-11 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_remove_customersendback_branch_and_more'),
        ('users', '0002_remove_customer_name_customer_first_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]