# Generated by Django 4.2.4 on 2023-10-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='service_id',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='service_type',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
