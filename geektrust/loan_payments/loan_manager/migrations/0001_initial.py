# Generated by Django 3.2.6 on 2021-08-12 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BANKS',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CUSTOMERS',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('loan_limit', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='QUERY_LOG',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('log', models.TextField()),
                ('when', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LOANS',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=20)),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('period', models.IntegerField()),
                ('period_months', models.IntegerField()),
                ('repaid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('emi_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount_PI', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bankid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan_manager.banks')),
                ('customerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan_manager.customers')),
            ],
        ),
    ]