from django.contrib import admin
from .models import (
    Participante, Vinculo, Participante_Vinculo, Atividade, Participante_Atividade, Terapeuta)


admin.site.register(Participante)
admin.site.register(Vinculo)
admin.site.register(Participante_Vinculo)
admin.site.register(Atividade)
admin.site.register(Participante_Atividade)
admin.site.register(Terapeuta)
