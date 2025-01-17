# Generated by Django 4.2.7 on 2023-11-14 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('matricula', models.CharField(max_length=11)),
                ('curso', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=80)),
                ('nacionalidade', models.CharField(max_length=25)),
                ('data_nascimento', models.DateField(max_length=8)),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=9)),
                ('periodo', models.CharField(choices=[('1°', '1°'), ('2°', '2°'), ('3°', '3°'), ('4°', '4°'), ('5°', '5°'), ('6°', '6°'), ('7°', '7°'), ('8°', '8°'), ('9°', '9°'), ('10°', '10°')], max_length=10)),
            ],
        ),
    ]
