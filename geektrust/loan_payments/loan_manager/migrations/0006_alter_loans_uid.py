# Generated by Django 3.2.6 on 2021-08-13 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_manager', '0005_auto_20210813_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loans',
            name='uid',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
