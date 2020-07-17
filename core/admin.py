from django.contrib import admin
from .models import (
    Pessoa, Vinculo, Pessoa_Vinculo, Atividade, Pessoa_Atividade, Terapeuta)


admin.site.register(Pessoa)
admin.site.register(Vinculo)
admin.site.register(Pessoa_Vinculo)
admin.site.register(Atividade)
admin.site.register(Pessoa_Atividade)
admin.site.register(Terapeuta)
