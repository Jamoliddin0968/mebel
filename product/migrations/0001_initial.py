# Generated by Django 4.1.7 on 2023-03-01 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '__first__'),
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField(verbose_name='Narxi')),
                ('total_sum', models.IntegerField(default=0, verbose_name='Summa')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Vaqt')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='branch.branch', verbose_name='Filial')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.customer', verbose_name='Xaridor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Hodim')),
            ],
            options={
                'verbose_name': 'Buyurtma',
                'verbose_name_plural': 'Buyurtmalar',
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Prixod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_sum', models.IntegerField(verbose_name='Summa')),
                ('date', models.DateTimeField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='branch.branch', verbose_name='Filial')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.provider')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Kirim hujjati',
                'verbose_name_plural': 'Kirimlar',
                'db_table': 'receive',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nomi')),
                ('material', models.CharField(max_length=255, verbose_name='Materiali')),
                ('size', models.CharField(max_length=255, verbose_name="O'lchami")),
                ('selling_price', models.PositiveIntegerField(verbose_name='Sotish narxi')),
                ('color', models.CharField(max_length=255, verbose_name='Rangi')),
                ('comment', models.CharField(max_length=255, verbose_name='Izoh')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Sotib olish narxi')),
                ('is_order', models.BooleanField(default=False, verbose_name='Buyurtma')),
                ('is_set', models.BooleanField(default=False, verbose_name='Komplektmi')),
            ],
            options={
                'verbose_name': 'Mahslulot',
                'verbose_name_plural': 'Mahsulotlar',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_sum', models.IntegerField(verbose_name='Summa')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='branch.branch', verbose_name='Filial')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.customer', verbose_name='Xaridor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Xodim')),
            ],
            options={
                'verbose_name': 'Sotuvlar',
                'verbose_name_plural': 'Sotuvlar',
                'db_table': 'sell',
            },
        ),
        migrations.CreateModel(
            name='SellItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Miqdori')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Mahsulot')),
                ('sell', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.sell', verbose_name='Sotuv hujjati')),
            ],
            options={
                'verbose_name': 'Sotuv tarkibi',
                'db_table': 'sell_item',
            },
        ),
        migrations.CreateModel(
            name='PrixodItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('prixod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.prixod', verbose_name='Prixod')),
            ],
            options={
                'verbose_name': 'Prixod tarkibi',
                'verbose_name_plural': 'Prixodlar tarkibi',
                'db_table': 'receive_items',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Miqdori')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.order', verbose_name='Buyurtma')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Tovar')),
            ],
            options={
                'verbose_name': 'Buyutma tarkibi',
                'verbose_name_plural': 'Buyutmalar tarkibi',
                'db_table': 'order_items',
            },
        ),
    ]