# Generated by Django 5.0.2 on 2024-03-14 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprestimo',
            old_name='id_livro',
            new_name='livro',
        ),
        migrations.RenameField(
            model_name='emprestimo',
            old_name='id_usuario',
            new_name='usuario',
        ),
        migrations.RemoveField(
            model_name='emprestimo',
            name='id_emprestimo',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='id_livro',
        ),
    ]
