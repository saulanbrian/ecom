# Generated by Django 5.0.1 on 2024-03-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_date_placed_order_date_received'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_placed',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]