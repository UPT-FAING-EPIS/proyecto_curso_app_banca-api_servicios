# Generated by Django 4.2 on 2023-06-10 05:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_factura_fecha_vencimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fecha_vencimiento',
            field=models.DateField(default=datetime.date(2023, 7, 10)),
        ),
    ]
