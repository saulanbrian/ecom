# Generated by Django 5.0.1 on 2024-02-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_product_rating_ave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating_ave',
            field=models.DecimalField(decimal_places=1, editable=False, max_digits=2, null=True),
        ),
    ]