# Generated by Django 4.1.7 on 2023-03-01 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nomi')),
                ('adress', models.CharField(max_length=150, verbose_name='Manzili')),
            ],
            options={
                'verbose_name': 'Filial',
                'verbose_name_plural': 'Filiallr',
                'db_table': 'branchs',
            },
        ),
    ]
