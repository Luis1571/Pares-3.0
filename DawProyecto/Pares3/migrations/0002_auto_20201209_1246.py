# Generated by Django 3.1 on 2020-12-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pares3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='imagen',
            field=models.ImageField(upload_to='Archivo'),
        ),
    ]