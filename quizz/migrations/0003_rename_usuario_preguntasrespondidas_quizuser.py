# Generated by Django 4.1.4 on 2023-01-09 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0002_quizusuario_preguntasrespondidas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preguntasrespondidas',
            old_name='usuario',
            new_name='quizUser',
        ),
    ]
