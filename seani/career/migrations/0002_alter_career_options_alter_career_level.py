# Generated by Django 5.0.2 on 2024-02-16 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='career',
            options={'verbose_name': 'carrera', 'verbose_name_plural': 'carreras'},
        ),
        migrations.AlterField(
            model_name='career',
            name='level',
            field=models.CharField(choices=[('Ing', 'Ingeniería'), ('TSU', 'Tecnico Superior Universitario'), ('M', 'Maestría')], max_length=10, verbose_name='Nivel'),
        ),
    ]
