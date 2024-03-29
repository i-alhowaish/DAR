# Generated by Django 5.0.1 on 2024-02-24 16:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_alter_property_neighborhood_alter_property_street'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyImages360',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image360', models.ImageField(upload_to='property_images360/')),
                ('property360', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images360', to='webapp.property')),
            ],
        ),
    ]
