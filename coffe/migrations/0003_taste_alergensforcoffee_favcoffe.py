# Generated by Django 5.1.3 on 2024-12-11 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffe', '0002_rename_conent_coffe_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AlergensForCoffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('coffe_cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='coffe.coffe')),
            ],
        ),
        migrations.CreateModel(
            name='FavCoffe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='coffe.category')),
            ],
        ),
    ]