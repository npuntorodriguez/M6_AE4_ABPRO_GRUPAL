from django.db import models
from django.core.validators import MaxLengthValidator, EmailValidator

class Evento(models.Model):
    """
    Modelo para representar un evento.
    """
    nombre = models.CharField(
        max_length=100,  # Máximo 100 caracteres
        verbose_name="Nombre del Evento",
        null=False,  # Equivalente a NOT NULL en SQL
        blank=False  # Obligatorio en el formulario
    )
    fecha = models.DateField(
        verbose_name="Fecha del Evento",
        null=False,  # Equivalente a NOT NULL en SQL
        blank=False  # Obligatorio en el formulario
    )
    ubicacion = models.CharField(
        max_length=200,
        verbose_name="Ubicación",
        null=True,  # Permite NULL en la base de datos
        blank=True  # Opcional en el formulario
    )

    def __str__(self):
        return f"{self.nombre} ({self.fecha})"

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['-fecha']

class Participante(models.Model):
    """
    Modelo para representar un participante en un evento.
    """
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name="participantes",
        verbose_name="Evento Asociado",
        null=False,  # Equivalente a NOT NULL en SQL
        blank=False,  # Obligatorio en el formulario
        default=1  # ID del evento por defecto (ajusta según tu base de datos)
    )
    nombre = models.CharField(
        max_length=100,
        verbose_name="Nombre del Participante",
        null=False,  # Equivalente a NOT NULL en SQL
        blank=False  # Obligatorio en el formulario
    )
    correo = models.EmailField(
        verbose_name="Correo Electrónico",
        null=False,  # Equivalente a NOT NULL en SQL
        blank=False,  # Obligatorio en el formulario
        validators=[EmailValidator(message="Ingresa un correo electrónico válido.")]
    )

    def __str__(self):
        return f"{self.nombre} ({self.correo})"

    class Meta:
        verbose_name = "Participante"
        verbose_name_plural = "Participantes"
        unique_together = [['evento', 'correo']]  # Evita participantes duplicados en un mismo evento
