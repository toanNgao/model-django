# Generated by Django 3.2.8 on 2021-10-29 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
    ]
