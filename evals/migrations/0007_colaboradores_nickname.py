# Generated by Django 5.0.6 on 2024-05-14 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evals', '0006_eventos_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaboradores',
            name='nickname',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]