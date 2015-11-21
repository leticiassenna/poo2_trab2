from django.contrib import admin
from capoeira.models import Aluno
from capoeira.models import Corda
from capoeira.models import Endereco
from capoeira.models import Exame
from capoeira.models import Grupo
from capoeira.models import Pessoa
from capoeira.models import Professor
from capoeira.models import Turma

# Register your models here.
class CadastroAluno(admin.ModelAdmin):
    model=Aluno
    list_display = ['nome', 'rg', 'cor_corda', 'grupo']
    search_fields = ['nome']
    save_on_top = True
admin.site.register(Aluno, CadastroAluno)

class CadastroProfessor(admin.ModelAdmin):
    model=Professor
    list_display = ['nome', 'rg', 'cor_corda', 'registro']
    search_fields = ['nome']
    save_on_top = True
admin.site.register(Professor, CadastroProfessor)

class CadastroGrupo(admin.ModelAdmin):
    model=Grupo
    list_display = ['nome', 'sequencia_corda']
    search_fields = ['nome']
    save_on_top = True
admin.site.register(Grupo, CadastroGrupo)

class CadastroTurma(admin.ModelAdmin):
    model=Turma
    list_display = ['nome', 'horario', 'dia_semana', 'professor']
    search_fields = ['nome']
    save_on_top = True
admin.site.register(Turma, CadastroTurma)
