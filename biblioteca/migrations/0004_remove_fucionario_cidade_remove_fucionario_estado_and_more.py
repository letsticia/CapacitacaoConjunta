# Generated by Django 5.0.2 on 2024-03-24 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_remove_usuario_endereço_remove_usuario_idade_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fucionario',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='fucionario',
            name='estado',
        ),
        migrations.AddField(
            model_name='fucionario',
            name='cidade_estado',
            field=models.CharField(default='Cidade/Estado', max_length=255),
        ),
        migrations.AlterField(
            model_name='fucionario',
            name='cpf',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='fucionario',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='fucionario',
            name='nome_completo',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='fucionario',
            name='senha',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='fucionario',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
    ]
