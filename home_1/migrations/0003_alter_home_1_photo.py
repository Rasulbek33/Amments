# Generated by Django 5.0 on 2023-12-15 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_1', '0002_alter_home_1_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_1',
            name='photo',
            field=models.ImageField(blank=True, upload_to='home_1/images'),
        ),
    ]
