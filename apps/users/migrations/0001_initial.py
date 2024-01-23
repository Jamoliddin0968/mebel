# Generated by Django 4.1.7 on 2024-01-23 05:03

import apps.users.models
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'Bu username bazada mavjud'}, max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='Ism')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Familiya')),
                ('patronymic', models.CharField(max_length=31, null=True, verbose_name='Otasining ismi')),
                ('phone', models.CharField(max_length=15, null=True, verbose_name='Telefon raqami')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='Manzili')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Hodim',
                'verbose_name_plural': 'Hodimlar',
            },
            managers=[
                ('objects', apps.users.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='F.I.SH')),
                ('corporation', models.CharField(max_length=255, verbose_name='Corporation')),
                ('address', models.CharField(max_length=255, verbose_name='Manzili')),
                ('phone', models.CharField(max_length=255, verbose_name='Telefon raqami')),
            ],
            options={
                'verbose_name': "Ta'minotchi",
                'verbose_name_plural': "Ta'minotchilar",
                'db_table': 'provider',
            },
        ),
        migrations.CreateModel(
            name='AllowedUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Hodim')),
            ],
            options={
                'verbose_name': 'Ruxsat berilgan',
                'verbose_name_plural': 'Ruxsat berilganlar',
            },
        ),
    ]
