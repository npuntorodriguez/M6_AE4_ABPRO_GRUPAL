from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .models import Evento, Participante
from .forms import EventoForm, ParticipanteForm

def index(request):
    eventos = Evento.objects.all().order_by('-fecha')
    participantes = Participante.objects.all()
    return render(request, 'index.html', {'eventos': eventos})

def registrar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save()  # Guarda el evento en la base de datos.
            return redirect('exito', evento_id=evento.id)  # Redirige al formulario de participantes.
    else:
        form = EventoForm()
    return render(request, 'eventos.html', {'form': form})

def registrar_participante(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            participante = form.save(commit=False)
            participante.evento = evento
            try:
                participante.save()
                return redirect('exito', evento_id=evento.id)
            except IntegrityError:
                form.add_error('correo', "Este correo electrónico ya está registrado para este evento.")
    else:
        form = ParticipanteForm()
    return render(request, 'participantes.html', {'form': form, 'evento': evento})

def exito(request, evento_id):
    return render(request, 'my_app/formulario_exitoso.html', {'evento_id': evento_id})
