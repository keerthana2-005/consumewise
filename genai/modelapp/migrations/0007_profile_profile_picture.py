# Generated by Django 5.1.1 on 2024-09-30 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0006_profile_blood_pressure_profile_diabetes'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics/'),
        ),
    ]
