# Generated by Django 4.2 on 2023-05-01 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_name', models.CharField(max_length=250, unique=True)),
                ('year', models.CharField(max_length=50)),
                ('specialty', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=250, unique=True)),
                ('year', models.CharField(max_length=50)),
                ('specialty', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=50)),
            ],
        ),
    ]
