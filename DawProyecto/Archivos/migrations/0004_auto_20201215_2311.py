# Generated by Django 3.1 on 2020-12-15 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Archivos', '0003_remove_archivo_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivo',
            name='descripcion',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='archivo',
            name='email',
            field=models.EmailField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='archivo',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
