# Generated by Django 5.0.6 on 2024-05-15 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evals', '0009_remove_avaliados_comments_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliados',
            name='evaluated_id',
        ),
        migrations.AddField(
            model_name='avaliados',
            name='evaluated_id',
            field=models.ManyToManyField(to='evals.colaboradores'),
        ),
    ]