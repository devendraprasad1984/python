# Generated by Django 3.2.6 on 2021-08-13 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SUBSCRIPTION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('secret_key', models.TextField(null=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]