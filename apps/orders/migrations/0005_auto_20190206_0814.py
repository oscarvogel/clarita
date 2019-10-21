# Generated by Django 2.1.3 on 2019-02-06 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190126_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='lugarentrega',
            field=models.CharField(choices=[('A', 'Retira'), ('O', 'Reparto')], default='O', max_length=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='ciudad',
            field=models.CharField(choices=[('Puerto Rico', 'Puerto Rico')], default='', max_length=100),
        ),
    ]