# Generated by Django 2.1.3 on 2019-01-11 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_auto_20190110_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalidadEntrega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('montominimoflete', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Paramsist',
            fields=[
                ('clave', models.CharField(db_column='clave', max_length=30, primary_key=True, serialize=False)),
                ('valor', models.CharField(max_length=100)),
                ('detalle', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'paramsist',
                'ordering': ('clave',),
            },
        ),
        migrations.AlterField(
            model_name='historial',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
