from django.db import models


# Create your models here.
class Student(models.Model):
    """
    Classe responsável pelo cadastro de alunos
    """
    nome = models.CharField(max_length=50, blank=False)
    matricula = models.CharField(max_length=11, blank=False)
    curso = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=80, blank=False)
    nacionalidade = models.CharField(max_length=25, blank=False)
    data_nascimento = models.DateField(max_length=8, blank=False)
    sexo = models.CharField(max_length=9, blank=False, choices=[("Masculino", "Masculino"), ("Feminino", "Feminino")])
    periodo = models.CharField(max_length=10, blank=False, choices=[("1°", "1°"), ("2°", "2°"), ("3°", "3°"), ("4°", "4°"), ("5°", "5°"), ("6°", "6°"), ("7°", "7°"), ("8°", "8°"), ("9°", "9°"), ("10°", "10°")])