from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('eventos/', views.registrar_evento, name='registrar_evento'),
    path('participantes/<int:evento_id>/', views.registrar_participante, name='registrar_participante'),
    path('exito/<int:evento_id>/', views.exito, name='exito'),  # Corrige aquí
    ]