# Generated by Django 5.1 on 2024-12-03 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('idreceta', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('idpaciente', models.CharField(max_length=100)),
                ('idmedico', models.CharField(max_length=100)),
                ('fechareceta', models.CharField(max_length=100)),
                ('instrucciones', models.CharField(max_length=100)),
                ('validez', models.CharField(max_length=100)),
                ('idmedicamento', models.CharField(max_length=100)),
            ],
        ),
    ]
