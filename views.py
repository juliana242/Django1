# views.py
from django.shortcuts import render
from .forms import ContactoForm

def formulario_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el objeto en la base de datos
    else:
        form = ContactoForm()
    return render(request, 'formulario_contacto.html', {'form': form})

