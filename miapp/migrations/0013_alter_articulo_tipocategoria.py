# Generated by Django 4.2.4 on 2023-09-17 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0012_articulo_tipocategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='tipoCategoria',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Computación'), (2, 'Componentes'), (3, 'Accesorios')], max_length=30),
        ),
    ]
