# Generated by Django 4.1 on 2022-09-09 06:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_tareas', '0004_alter_tarea_fechaentrega'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fechaCreacion',
            field=models.DateField(default=datetime.datetime(2022, 9, 9, 1, 23, 15, 514727)),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fechaEntrega',
            field=models.DateField(default=datetime.datetime(2022, 9, 9, 1, 23, 15, 514727)),
        ),
    ]