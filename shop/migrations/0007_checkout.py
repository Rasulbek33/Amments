# Generated by Django 5.0 on 2023-12-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_compare'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('sub_title', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Checkout',
                'verbose_name_plural': 'Checkouts',
            },
        ),
    ]
