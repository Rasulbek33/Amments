# Generated by Django 5.0 on 2023-12-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_product_detail_photo_3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='product_group/images')),
                ('photo_title', models.CharField(blank=True, max_length=255)),
                ('photo_sub_title', models.CharField(blank=True, max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('photo_1', models.ImageField(blank=True, upload_to='product_group/photo_1')),
                ('photo_1_about', models.CharField(blank=True, max_length=255)),
                ('photo_2', models.ImageField(blank=True, upload_to='product_group/photo_2')),
            ],
        ),
    ]