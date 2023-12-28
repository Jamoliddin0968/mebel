# Generated by Django 4.1.7 on 2023-12-28 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
        ('orders', '0003_orderimages_order_is_notificated_order_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='notification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='notifications.schedulednotification'),
        ),
    ]