# Generated by Django 4.2.8 on 2024-01-30 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BMImodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(max_length=10, verbose_name='Weight')),
                ('height', models.FloatField(max_length=10, verbose_name='Height')),
            ],
        ),
    ]