# Generated by Django 5.0.2 on 2024-06-25 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0015_pedido_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
