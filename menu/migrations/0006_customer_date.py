# Generated by Django 4.2.4 on 2023-10-07 16:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_remove_customer_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
