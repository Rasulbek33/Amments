# Generated by Django 5.0 on 2023-12-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grid_sidebar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('sub_title', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Grid_sidebar',
                'verbose_name_plural': 'Grid_sidebars',
            },
        ),
    ]
