from django import forms
from django.core.exceptions import ValidationError
from .models import Evento, Participante
from django.utils import timezone

class EventoForm(forms.ModelForm):
    """
    Formulario para registrar eventos.
    """
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'ubicacion']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_nombre(self):
        """
        Valida que el nombre del evento no supere los 100 caracteres.
        """
        nombre = self.cleaned_data['nombre']
        if len(nombre) > 100:
            raise ValidationError("El nombre del evento no debe superar los 100 caracteres.")
        return nombre

    def clean_fecha(self):
        """
        Valida que la fecha del evento sea futura.
        """
        fecha = self.cleaned_data['fecha']
        if fecha < timezone.now().date():
            raise ValidationError("La fecha del evento debe ser futura.")
        return fecha

class ParticipanteForm(forms.ModelForm):
    """
    Formulario para registrar participantes.
    """
    class Meta:
        model = Participante
        fields = ['nombre', 'correo']

    def __init__(self, *args, **kwargs):
        self.evento = kwargs.pop('evento', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        correo = cleaned_data.get('correo')
        if self.evento and correo:
            if Participante.objects.filter(evento=self.evento, correo=correo).exists():
                raise ValidationError("Ya existe un participante con este correo en el evento.")
        return cleaned_data