# Generated by Django 5.0.2 on 2024-02-14 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_remove_question_text_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'verbose_name': 'módulo', 'verbose_name_plural': 'módulos'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'pregunta', 'verbose_name_plural': 'preguntas'},
        ),
        migrations.AlterField(
            model_name='question',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.module', verbose_name='Módulo'),
        ),
    ]
