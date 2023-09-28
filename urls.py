# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Otras URL de la aplicación
    path('contacto/', views.vista_contacto, name='vista_contacto'),
]
