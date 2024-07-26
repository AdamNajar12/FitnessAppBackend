# Generated by Django 5.0.7 on 2024-07-15 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programs', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('duree', models.IntegerField()),
                ('repetitions', models.IntegerField()),
                ('sets', models.IntegerField()),
                ('verrouillage', models.BooleanField(default=False)),
                ('programme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercices', to='programs.programs')),
            ],
        ),
        migrations.CreateModel(
            name='Porteuse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('note', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='porteuses', to='users.client')),
                ('exercice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='porteuses', to='exercises.exercice')),
            ],
        ),
    ]
