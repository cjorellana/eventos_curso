from django.shortcuts import render,get_object_or_404, redirect
from .models import evento,Contacto
from django.contrib import messages

# Create your views here. 
def home(request):

    listado_eventos = evento.objects.all().order_by('fecha_Inicio')
    #listado_eventos = evento.objects.filter(activo=True).order_by('fecha_Inicio')
    #sql= "select * from eventos_evento where activo=True order by fecha_Inicio;"

    #print(len(listado_eventos))
    #print(type(listado_eventos))

    data = {
        'title': 'Listado de eventos',
        'listado': listado_eventos,
    }

    # data= {
    #     'title': 'Listado de eventos',
    #     'description': 'Bienvenido a la página de eventos',
    #     'events': [
    #         {'name': 'Concierto de Rock', 'date': '2023-10-01', 'location': 'Estadio Municipal'},
    #         {'name': 'Feria de Comida', 'date': '2023-10-15', 'location': 'Parque Central'},
    #         {'name': 'Conferencia de Tecnología', 'date': '2023-11-05', 'location': 'Centro de Convenciones'},
    #     ]
    # }
    return render(request, 'home.html', data)

#busqueda de producto
def buscar(request):
    nombre = request.POST.get('nombre', '')

    print(nombre)

    if nombre:
        listado_eventos = evento.objects.filter(nombre__icontains=nombre).order_by('fecha_Inicio')
    else:
        listado_eventos = evento.objects.all().order_by('fecha_Inicio')

    data = {
        'title': 'Eventos encontrados ...',
        'listado': listado_eventos,
    }    
    return render(request, 'home.html', data)


def about(request):
    return render(request, 'about.html')



def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        correo = request.POST.get('email', '')
        mensaje = request.POST.get('mensaje', '')
        tipo = request.POST.get('tipo', '1')

       

        try:
             # Validar los datos del formulario
            if not nombre:
                messages.error(request, 'Debes ingresar tu nombre.')
            else:
                contacto = Contacto(nombre=nombre, correo=correo, mensaje=mensaje, tipo=tipo)
                contacto.save()   
                messages.success(request, 'Se guardó el reporte correctamente.')
        except Exception as e:
            messages.error(request, f'Error al guardar el Reporte: {e}')

        # Aquí podrías procesar el formulario, como enviar un correo electrónico o guardar en la base de datos
        #print(f'Nombre: {nombre}, Email: {email}, Mensaje: {mensaje}')
        #guardar en la base de datos o enviar un correo electrónico
    

        # Redirigir a una página de agradecimiento o mostrar un mensaje de éxito
        #return redirect('home')

    return render(request, 'contacto.html')

def detalle(request, id=None):
    #objproducto = get_object_or_404(Producto, pk=id)
    if id is None:
        return redirect('home')
    
    listado_eventos = get_object_or_404(evento, pk=id) 

    
    data = {
        'title': 'Detalle del evento',
        'listado': listado_eventos,
    }   

    return render(request, 'detalle.html', data)