from django.shortcuts import render
from .models import evento

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

def about(request):
    return render(request, 'about.html')