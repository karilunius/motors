# Generated by Django 4.1.2 on 2022-10-06 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clientes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clientes", name="cedula_cliente", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="clientes", name="telefono_cliente", field=models.IntegerField(),
        ),
    ]
