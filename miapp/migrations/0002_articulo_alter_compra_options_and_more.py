# Generated by Django 4.2.4 on 2023-08-27 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Artículo',
                'verbose_name_plural': 'Artículos',
            },
        ),
        migrations.AlterModelOptions(
            name='compra',
            options={'verbose_name': 'Compra', 'verbose_name_plural': 'Compras'},
        ),
        migrations.AlterModelOptions(
            name='comprobante',
            options={'verbose_name': 'Comprobante', 'verbose_name_plural': 'Comprobantes'},
        ),
        migrations.AlterModelOptions(
            name='datosfacturacion',
            options={'verbose_name': 'Dato Facturacion', 'verbose_name_plural': 'Datos de Facturación'},
        ),
        migrations.AlterModelOptions(
            name='datospersonales',
            options={'ordering': ['nombre', 'claseFiscalTipo'], 'verbose_name': 'Dato Personal', 'verbose_name_plural': 'Datos Personales'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'Usuarios', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.RemoveField(
            model_name='compra',
            name='comprobante',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='detalle',
        ),
        migrations.CreateModel(
            name='ArticuloCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.articulo')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.compra')),
            ],
            options={
                'verbose_name': 'Artículo en Compra',
                'verbose_name_plural': 'Artículos en Compras',
            },
        ),
        migrations.AddField(
            model_name='compra',
            name='articulos',
            field=models.ManyToManyField(through='miapp.ArticuloCompra', to='miapp.articulo'),
        ),
    ]
