# Generated by Django 5.0.1 on 2024-02-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic2',
            field=models.ImageField(upload_to='profile/images'),
        ),
    ]
