# Generated by Django 4.2.1 on 2023-05-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='storageMemory',
            field=models.CharField(max_length=50),
        ),
    ]
