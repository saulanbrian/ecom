# Generated by Django 5.0.1 on 2024-03-05 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_product_rating_ave'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
