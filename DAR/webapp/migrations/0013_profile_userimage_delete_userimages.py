# Generated by Django 5.0.1 on 2024-03-20 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_profile_alter_favorite_uid_alter_property_uid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='userimage',
            field=models.ImageField(blank=True, null=True, upload_to='static/user_images/'),
        ),
        migrations.DeleteModel(
            name='userImages',
        ),
    ]
