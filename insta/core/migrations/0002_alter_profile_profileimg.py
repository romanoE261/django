# Generated by Django 4.2.5 on 2023-11-16 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='logo.png', upload_to='profile_images'),
        ),
    ]
