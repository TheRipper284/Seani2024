# Generated by Django 5.0.2 on 2024-02-14 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_module_options_alter_question_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.module', verbose_name='Módulo'),
        ),
    ]
