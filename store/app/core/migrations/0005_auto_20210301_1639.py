# Generated by Django 3.1 on 2021-03-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_category_customer_orders_products_seller_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(max_length=255),
        ),
    ]
