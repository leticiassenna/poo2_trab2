from django.db import models
# Create your models here.

class Endereco(models.Model):
    logradouro = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)

class Grupo(models.Model):
    sequencia_corda = models.CharField(max_length=100)
    nome = models.CharField(max_length=100, primary_key=True)
    endereco = models.ForeignKey(Endereco)

class Pessoa(models.Model):
	nome = models.CharField(max_length=100)
	rg = models.CharField(max_length=20)
	data_nascimento = models.DateField()
	endereco = models.ForeignKey(Endereco)
	telefone = models.CharField(max_length=50)
	profissao = models.CharField(max_length=50)
	grau_escolar = models.CharField(max_length=50)
	cor_corda = models.CharField(max_length=50)
	grupo = models.ForeignKey(Grupo)


class Aluno(Pessoa):
        pai = models.CharField(max_length=100)
        mae = models.CharField(max_length=100)

class Professor(Pessoa):
    registro = models.CharField(max_length=100)

class Turma(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)
    turno = models.CharField(max_length=100)
    horario = models.DateField()
    dia_semana = models.CharField(max_length=100)
    aluno = models.ForeignKey(Aluno) #verificar a necessidade de criacao de uma tabela relacional(n p/ n)
	#Try it: models.ManyToManyField(ClassName)
    professor = models.ForeignKey(Professor)

class Exame(models.Model):
    data = models.DateField() #Considerando que data e hora estao contidos no mesmo campo
    endereco = models.ForeignKey(Endereco)
    mestre_examinador = models.CharField(max_length=100)
    turma = models.ForeignKey(Turma)

class Corda(models.Model):
	cor = models.CharField(max_length=100, primary_key=True)
