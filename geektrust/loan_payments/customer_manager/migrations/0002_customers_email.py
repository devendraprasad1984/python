# Generated by Django 3.2.6 on 2021-08-13 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
