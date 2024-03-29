# Generated by Django 4.1.7 on 2024-01-23 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('warehouses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WareHouseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouses.warehouse')),
            ],
        ),
    ]
