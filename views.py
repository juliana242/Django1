# views.py

from django.shortcuts import render
from .forms import Formulariocontacto

def vista_contacto(request):
    if request.method == 'POST':
        form = Formulariocontacto(request.POST)
        if form.is_valid():
            # Procesar el formulario si es válido
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            mensaje = form.cleaned_data['mensaje']
            # Puedes realizar acciones adicionales aquí, como enviar un correo electrónico o guardar en la base de datos
    else:
        # Mostrar un formulario en blanco si no se ha enviado
        form = Formulariocontacto()

    return render(request, 'formulario_contacto.html', {'form': form})
