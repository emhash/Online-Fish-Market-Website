# Generated by Django 5.0.7 on 2024-07-28 18:47

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_remove_profile_area_remove_profile_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('area', models.CharField(blank=True, max_length=100)),
                ('post_code', models.CharField(blank=True, max_length=100)),
                ('phone_no', models.PositiveIntegerField(blank=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]