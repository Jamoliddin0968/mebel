# Generated by Django 4.1.7 on 2024-01-30 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image.image'),
        ),
    ]