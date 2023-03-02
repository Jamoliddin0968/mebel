# Generated by Django 4.1.7 on 2023-03-02 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_customersendback_alter_prixod_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customersendbackitems',
            options={'verbose_name': 'Xaridorga vozvrat hujjati tarkibi', 'verbose_name_plural': 'Xaridorga vozvrat hujjati tarkibi'},
        ),
        migrations.AlterField(
            model_name='customersendbackitems',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Narxi'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Narxi'),
        ),
        migrations.AlterField(
            model_name='prixoditems',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Narxi'),
        ),
        migrations.AlterField(
            model_name='providersendbackitems',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Narxi'),
        ),
        migrations.AlterField(
            model_name='sellitem',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Narxi'),
        ),
    ]