# Generated by Django 4.2.8 on 2024-02-28 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopsite', '0002_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]