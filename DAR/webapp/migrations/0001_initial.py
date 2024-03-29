# Generated by Django 5.0.1 on 2024-02-16 10:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('furnished', models.BooleanField()),
                ('number_of_bathrooms', models.IntegerField()),
                ('region', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
                ('coordinate', models.CharField(max_length=100)),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('width', models.DecimalField(decimal_places=2, max_digits=10)),
                ('number_of_sides', models.IntegerField()),
                ('facade', models.CharField(max_length=100)),
                ('number_of_rooms', models.IntegerField()),
                ('sell_or_rent', models.CharField(max_length=50)),
                ('number_of_parkings', models.IntegerField()),
                ('number_of_bedrooms', models.IntegerField()),
                ('year_built', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RealEstateTransactions',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('classification', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('number_of_properties', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('size', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='property_images/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='webapp.property')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('us', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.property')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.user'),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.property')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.user')),
            ],
        ),
    ]
