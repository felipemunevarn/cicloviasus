# Generated by Django 4.2.3 on 2024-03-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.CharField(blank=True, default=None, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(blank=True, default=None, max_length=999, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
