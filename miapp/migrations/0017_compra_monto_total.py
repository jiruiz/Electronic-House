# Generated by Django 4.2.4 on 2023-09-26 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0016_articulo_tipocategoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='monto_total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
