# Generated by Django 5.0.1 on 2024-02-05 19:57

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('discription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='category_gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('filter', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EducationAndExpericence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('place_name', models.CharField(max_length=50)),
                ('year_from', models.DateField()),
                ('year_to', models.DateField()),
                ('categoryes', models.CharField(choices=[('expericence', 'Expericence'), ('education', 'Education')], max_length=13)),
                ('discription', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'education_expericence',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('pic', models.ImageField(upload_to='')),
                ('birthday', models.DateField()),
                ('experience', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=60)),
                ('degree', models.CharField(choices=[('university degree', 'university degree'), ('Masters degree', 'Masters degree'), ('Doctorate degree', 'Doctorate degree'), ('Vocational school', 'Vocational school'), ('High School', 'High School')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('icon_name', models.CharField(max_length=20)),
                ('discription', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('percent', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='picture_gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.category_gallery')),
            ],
        ),
    ]