# Generated by Django 5.0.6 on 2024-05-14 02:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaboradores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colaborador_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('function', models.CharField(max_length=100)),
                ('admission_date', models.DateField()),
                ('functional_group', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_id', models.IntegerField()),
                ('form', models.CharField(max_length=100)),
                ('range', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Resultados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.IntegerField()),
                ('result', models.IntegerField()),
                ('classification', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.IntegerField()),
                ('creation_date', models.DateField()),
                ('evaluator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evals.colaboradores')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions_id', models.IntegerField()),
                ('eval', models.IntegerField()),
                ('form_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evals.form')),
                ('result_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evals.resultados')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliados_id', models.IntegerField()),
                ('comments', models.CharField(max_length=1000)),
                ('evaluated_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evals.colaboradores')),
                ('evaluation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evals.eventos')),
                ('results_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evals.resultados')),
            ],
        ),
    ]
