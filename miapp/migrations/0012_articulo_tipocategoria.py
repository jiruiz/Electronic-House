# Generated by Django 4.2.4 on 2023-09-17 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0011_remove_articulo_categoria_delete_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='tipoCategoria',
            field=models.CharField(choices=[('Computacion', 'Computación'), ('Componentes', 'Componentes'), ('Accesorios', 'Accesorios')], default=1, max_length=30),
            preserve_default=False,
        ),
    ]
