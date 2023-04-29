# Generated by Django 4.2 on 2023-04-28 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('cuenta_bancaria', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroLlamadas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('duracion', models.PositiveIntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.cliente')),
            ],
        ),
    ]
