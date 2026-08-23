from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactoForm
from .models import Servicio

def inicio(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            correo = formulario.cleaned_data['correo']
            mensaje_usuario = formulario.cleaned_data['mensaje']
            
            # Preparamos el correo
            asunto = f"Nuevo mensaje web de: {nombre}"
            cuerpo = f"Has recibido un mensaje.\n\nNombre: {nombre}\nCorreo: {correo}\n\nMensaje:\n{mensaje_usuario}"
            remitente = 'sistema@gasesnobles.com' # Correo ficticio del sistema
            destinatarios = ['gerencia_admin@gasesnobles.com'] # <-- Aquí configuramos tu correo de destino
            
            # Ordenamos a Django enviar el correo
            send_mail(asunto, cuerpo, remitente, destinatarios)
            
            messages.success(request, '¡Tu mensaje ha sido enviado con éxito!')
            return redirect('inicio')
        pass    
    else:
        formulario = ContactoForm()
    servicions_db = Servicio.objects.all()
    contexto = {
        'empresa': 'Gases Nobles SAS',
        'servicios': servicions_db,
        'formulario': formulario
    }
    return render(request, 'portafolio/inicio.html', contexto)

def detalle_servicio(request, url_id):
    servicio_seleccionado = get_object_or_404(Servicio, identificador=url_id)
    return render(request, 'portafolio/detalle.html', {'servicio': servicio_seleccionado})