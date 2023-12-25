# Generated by Django 4.1.7 on 2023-12-25 15:34

import apps.products.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nomi')),
                ('price', models.FloatField(default=0, verbose_name='Sotib olish narxi')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_products', to='categories.category')),
            ],
            options={
                'verbose_name': 'Mahslulot',
                'verbose_name_plural': 'Mahsulotlar',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=apps.products.models.rename_image)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='products.product')),
            ],
        ),
    ]
