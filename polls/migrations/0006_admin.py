# Generated by Django 3.1.2 on 2020-12-25 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20201225_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('Id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('pas', models.BinaryField()),
            ],
        ),
    ]