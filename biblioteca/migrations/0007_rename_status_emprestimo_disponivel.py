# Generated by Django 5.0.2 on 2024-03-24 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0006_rename_status_livro_disponivel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprestimo',
            old_name='status',
            new_name='disponivel',
        ),
    ]