# Generated by Django 5.0.2 on 2024-03-08 23:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0009_rename_fecha_pedido_fecha_pedido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha_entrega',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateField(default=datetime.date(2024, 3, 8)),
        ),
    ]