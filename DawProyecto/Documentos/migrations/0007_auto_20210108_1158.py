# Generated by Django 3.1 on 2021-01-08 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documentos', '0006_auto_20201228_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='siglo',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]