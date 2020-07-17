from django.shortcuts import render
from ..forms import ParticipanteForm

# Create your views here.


def participante(request):
    form_participante = ParticipanteForm()
    return render(request, 'participante/form_participante.html', {
        "form_participante": form_participante})
