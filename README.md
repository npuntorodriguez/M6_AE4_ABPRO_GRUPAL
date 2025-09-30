# M6 AE4 ABPRO EJERCICIO GRUPAL

## Proyecto de Registro de Eventos con Django

Esta es una aplicación web desarrollada con Django que permite la gestión de eventos y el registro de participantes. Los usuarios pueden crear eventos, y para cada evento, se pueden registrar múltiples participantes, asegurando que no haya correos electrónicos duplicados por evento.

## Características

* **Creación de Eventos:** Formulario para añadir nuevos eventos con nombre, fecha y ubicación.
* **Registro de Participantes:** Formulario para registrar participantes en un evento específico, solicitando nombre y correo electrónico.
* **Listado de Eventos:** La página principal muestra todos los eventos existentes en tarjetas, junto con la lista de participantes inscritos en cada uno.
* **Validaciones:**

  * La fecha del evento debe ser futura.
  * No se permite registrar a un participante con el mismo correo electrónico más de una vez en el mismo evento.
* **Interfaz Amigable:** Uso de Bootstrap para un diseño limpio y responsivo.

## Tecnologías Utilizadas

* **Backend:** Python, Django
* **Base de Datos:** SQLite3
* **Frontend:** HTML, Bootstrap 5

## Instalación y Puesta en Marcha

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1. **Clona el repositorio:**

   ```bash

   git clone <URL_DEL_REPOSITORIO>

   cd registro_eventos

   ```
2. **Crea y activa un entorno virtual:**

   ```bash

   # Crea el entorno virtual

   python -m venv venv


   # Activa el entorno en Windows

   venv\Scripts\activate


   # Activa el entorno en macOS/Linux

   source venv/bin/activate

   ```
3. **Instala las dependencias:**

   Se recomienda tener un archivo `requirements.txt`. Por ahora, puedes instalar Django manualmente.

   ```bash

   pip install Django

   ```
4. **Aplica las migraciones:**

   Dentro del directorio `registro_eventos` (donde se encuentra `manage.py`):

   ```bash

   python manage.py migrate

   ```
5. **Crea un superusuario (opcional, para el panel de administración):**

   ```bash

   python manage.py createsuperuser

   ```
6. **Ejecuta el servidor de desarrollo:**

   ```bash

   python manage.py runserver

   ```

   Abre tu navegador y visita `http://127.0.0.1:8000/` para ver la aplicación en funcionamiento.

## Colaboradores

Este proyecto fue desarrollado por:

* Sofía Lagos ([too0oori](https://github.com/too0oori))
* Natalia Rodríguez ([npuntorodriguez](https://github.com/npuntorodriguez))
* Hans Schiess ([schiesscl](https://github.com/schiesscl))
* Johana Torres ([JATeR912](https://github.com/JATeR912))
