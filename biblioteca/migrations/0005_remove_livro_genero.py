# Generated by Django 5.0.2 on 2024-03-24 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0004_remove_fucionario_cidade_remove_fucionario_estado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='genero',
        ),
    ]
