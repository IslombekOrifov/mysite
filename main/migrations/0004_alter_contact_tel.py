# Generated by Django 4.2 on 2023-05-01 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contact_userletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tel',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
