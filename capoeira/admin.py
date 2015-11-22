from django.contrib import admin
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


