# Generated by Django 4.2.1 on 2023-07-07 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion7', '0003_alter_tarea_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('prevision', models.CharField()),
            ],
        ),
    ]