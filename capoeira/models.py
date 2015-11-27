from django.db import models
import copy

# Create your models here.

class Endereco(models.Model):
    logradouro = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    def __str__(self):
        return self.logradouro

class Grupo(models.Model):
    sequencia_corda = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco)
    def __str__(self):
        return self.nome
    def clone(self):
        return copy.copy(self)

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
    def __str__(self):
        return self.nome


class Aluno(Pessoa):
        pai = models.CharField(max_length=100)
        mae = models.CharField(max_length=100)
        def clone(self):
            return copy.copy(self)

class Professore(Pessoa):
    registro = models.CharField(max_length=100)
    def clone(self):
        return copy.copy(self)

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    turno = models.CharField(max_length=100)
    horario = models.DateField()
    dia_semana = models.CharField(max_length=100)
    aluno = models.ForeignKey(Aluno) #verificar a necessidade de criacao de uma tabela relacional(n p/ n)
	#Try it: models.ManyToManyField(ClassName)
    professor = models.ForeignKey(Professore)
    def __str__(self):
        return self.nome
    def clone(self):
        return copy.copy(self)

class Exame(models.Model):
    data = models.DateField() #Considerando que data e hora estao contidos no mesmo campo
    endereco = models.ForeignKey(Endereco)
    mestre_examinador = models.CharField(max_length=100)
    turma = models.ForeignKey(Turma)
    def __str__(self):
        return self.data
    def clone(self):
        return copy.copy(self)

class Corda(models.Model):
    cor = models.CharField(max_length=100)
    def __str__(self):
        return self.cor

class Fabrica(models.Model):
    exame = Exame()
    aluno = Aluno()
    professor = Professore()
    grupo = Grupo()
    turma=Turma()
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Fabrica, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def retornar_objeto(self, objeto):
        if objeto== "aluno":
            return self.__class__.aluno.clone()
        if objeto== "professor":
            return self.__class__.professor.clone()
        if objeto == "grupo":
            return self.__class__.grupo.clone()
        if objeto == "turma":
            return self.__class__.turma.clone()
        if objeto == "exame":
            return self.__class__.exame.clone()

class Flyweight(models.Model):
    objetos = {}
    def __new__(cls, *args, **kwargs):
         if not hasattr(cls, '_instance'):
            cls._instance = super(Flyweight, cls).__new__(cls, *args, **kwargs)
         return cls._instance
    def get_objeto(self, nome):
        objeto = self.__class__.objetos[nome]
        if objeto == None:
            self.__class__.objetos[nome] = Fabrica().retornar_objeto(nome)

        return objeto

class Relatorio(models.Model):
    def __new__(cls, *args, **kwargs):
         if not hasattr(cls, '_instance'):
             cls._instance = super(Relatorio, cls).__new__(cls, *args, **kwargs)
         return cls._instance

    def gerar_relatorio_aluno(self):
        aluno = Flyweight().get_objeto("aluno")
        alunos = Aluno.objects.all()
        arq = open("Relatorio Alunos.txt", "w")
        for aluno in alunos:
            arq.write(aluno.nome)
            arq.write("\n")
            arq.write(aluno.cor_corda)
            arq.write("\n")
            arq.write(aluno.grupo.nome)
            arq.write("\n")

        arq.close()


