# Generated by Django 3.1 on 2020-12-15 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Archivos', '0002_auto_20201212_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archivo',
            name='descripcion',
        ),
    ]