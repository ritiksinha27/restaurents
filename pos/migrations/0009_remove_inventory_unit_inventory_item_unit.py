# Generated by Django 4.2.6 on 2023-10-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0008_inventory_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='unit',
        ),
        migrations.AddField(
            model_name='inventory_item',
            name='unit',
            field=models.CharField(default='KG', max_length=12),
        ),
    ]
