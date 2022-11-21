from django.shortcuts import render
from core.models import Evento
# Create your views here.

def lista_eventos(request):
    dados = {}
    usuario = request.user
    dados['db'] = Evento.objects.filter(usuario=usuario)
    return render(request,'agenda.html',dados)