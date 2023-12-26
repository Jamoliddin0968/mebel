# Generated by Django 4.1.7 on 2023-12-25 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='view_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]