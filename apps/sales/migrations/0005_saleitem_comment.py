# Generated by Django 4.1.7 on 2024-01-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_alter_sale_datetime_alter_sale_price_saleitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleitem',
            name='comment',
            field=models.TextField(default=''),
        ),
    ]
