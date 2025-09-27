from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, Participante
from .forms import EventoForm, ParticipanteForm

def index(request):
    return render(request, 'index.html')

def registrar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save()  # Guarda el evento en la base de datos.
            return redirect('registrar_participantes', evento_id=evento.id)  # Redirige al formulario de participantes.
    else:
        form = EventoForm()
    return render(request, 'my_app/formulario_eventos.html', {'form': form})

def registrar_participantes(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)  # Obtiene el evento o retorna 404.
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            participante = form.save(commit=False)
            participante.evento = evento  # Asocia el participante al evento.
            participante.save()
            return redirect('exito')  # Redirige a la página de éxito.
    else:
        form = ParticipanteForm()
    return render(request, 'my_app/formulario_participantes.html', {'form': form, 'evento': evento})

def exito(request):
    return render(request, 'my_app/formulario_exitoso.html')
