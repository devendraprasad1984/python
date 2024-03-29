# Generated by Django 3.2.6 on 2021-08-13 04:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_manager', '0001_initial'),
        ('bank_manager', '0001_initial'),
        ('loan_manager', '0004_auto_20210812_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loans',
            name='bankid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_manager.banks'),
        ),
        migrations.AlterField(
            model_name='loans',
            name='customerid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_manager.customers'),
        ),
        migrations.DeleteModel(
            name='BANKS',
        ),
        migrations.DeleteModel(
            name='CUSTOMERS',
        ),
    ]
