# Generated by Django 3.1 on 2020-12-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documentos', '0005_auto_20201215_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='imagen',
            field=models.ImageField(null=True, upload_to='Documentos'),
        ),
    ]
