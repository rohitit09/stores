# Generated by Django 3.1 on 2021-02-27 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='store',
        ),
        migrations.AddField(
            model_name='store',
            name='products',
            field=models.ManyToManyField(blank=True, to='store.Products'),
        ),
    ]
