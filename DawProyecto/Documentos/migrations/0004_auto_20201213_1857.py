# Generated by Django 3.1 on 2020-12-13 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documentos', '0003_auto_20201213_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='idusuario',
        ),
        migrations.AddField(
            model_name='documento',
            name='conservacion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='documento',
            name='contenido',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='documento',
            name='titulo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='siglo',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
