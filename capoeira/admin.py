from django.contrib import admin
<<<<<<< HEAD
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
=======
from .models import Endereco
from .models import Grupo
from .models import Pessoa
from .models import Aluno
from .models import Professor
from .models import Turma
from .models import Corda

admin.site.register(Endereco)
admin.site.register(Grupo)
admin.site.register(Pessoa)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Turma)
admin.site.register(Corda)


>>>>>>> refs/remotes/brianebianca/master
