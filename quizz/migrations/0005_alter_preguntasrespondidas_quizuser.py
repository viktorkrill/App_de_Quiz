# Generated by Django 4.1.4 on 2023-01-09 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0004_pregunta_max_puntaje_alter_elegirrespuesta_pregunta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntasrespondidas',
            name='quizUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intentos', to='quizz.quizusuario'),
        ),
    ]