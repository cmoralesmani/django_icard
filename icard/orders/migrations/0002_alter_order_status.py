# Generated by Django 3.2.9 on 2021-12-27 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', 'pending'), ('DELIVERED', 'delivered')], max_length=255),
        ),
    ]
