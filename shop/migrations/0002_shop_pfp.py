# Generated by Django 5.0.3 on 2024-03-28 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='pfp',
            field=models.ImageField(null=True, upload_to='shop/images'),
        ),
    ]
