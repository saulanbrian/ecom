# Generated by Django 5.0.1 on 2024-03-01 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_placed',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='date_received',
            field=models.DateTimeField(null=True),
        ),
    ]
