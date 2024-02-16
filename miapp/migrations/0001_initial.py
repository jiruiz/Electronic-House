# Generated by Django 4.2.4 on 2023-08-26 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('idComprobante', models.AutoField(primary_key=True, serialize=False)),
                ('numeroComprobante', models.CharField(max_length=20, verbose_name='Número de Comprobante')),
                ('fechaEmision', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Comprobantes',
            },
        ),
        migrations.CreateModel(
            name='DatosFacturacion',
            fields=[
                ('idDatosFacturacion', models.AutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=100)),
                ('altura', models.CharField(max_length=10)),
                ('piso', models.CharField(blank=True, max_length=10)),
                ('departamento', models.CharField(blank=True, max_length=10)),
                ('codigoPostal', models.CharField(max_length=10)),
                ('localidad', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Datos de Facturación',
            },
        ),
        migrations.CreateModel(
            name='DatosPersonales',
            fields=[
                ('idDatosPersonales', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('claseFiscalTipo', models.CharField(choices=[('Consumidor Final', 'Consumidor Final'), ('Monotributo', 'Monotributo'), ('Responsable Inscripto', 'Responsable Inscripto'), ('Excento', 'Excento')], max_length=30)),
                ('numeroDocumento', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Datos Personales',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('datosFacturacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='miapp.datosfacturacion')),
                ('datosPersonales', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='miapp.datospersonales')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('idCompra', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('detalle', models.TextField()),
                ('comprobante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.comprobante')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.usuario')),
            ],
            options={
                'verbose_name_plural': 'Compras',
            },
        ),
    ]