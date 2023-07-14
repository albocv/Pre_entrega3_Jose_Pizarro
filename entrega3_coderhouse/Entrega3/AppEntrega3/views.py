from django.http import HttpResponse
from django.shortcuts import render
from AppEntrega3.models import Clientes,Arriendos
from AppEntrega3.forms import ClienteFormulario, ArriendoFormulario

# Create your views here.
#def cliente(self):
#    cliente = Clientes(nombre='Katherine', apellido='Leiva', direccion='Holanda 0298')
#    cliente.save()

#    documentoDeTexto = f'------->Cliente: {cliente.nombre} apellido: {cliente.apellido} direccion: {cliente.direccion}' 

#    return HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request, 'inicio.html')

def vistaClientes(request):
    return render(request, 'clientes.html')

def vistaPeliculas(request):
    return render(request, 'peliculas.html')

def vistaArriendos(request):
    return render(request, 'arriendos.html')

def clienteFormulario(request):
    if request.method == "POST":
        miFormulario = ClienteFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente = Clientes(nombre=informacion['nombre_cliente'],apellido=informacion['apellido_cliente'],direccion=informacion['direccion_cliente'])
            cliente.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = ClienteFormulario()

    return render(request, 'clientes.html', {"miFormulario": miFormulario})
    #return render(request, 'clienteFormulario.html', {"miFormulario": miFormulario})

def arriendoFormulario(request):
    if request.method == "POST":
        miFormulario2 = ArriendoFormulario(request.POST)
        print(miFormulario2)
        if miFormulario2.is_valid:
            informacion2 = miFormulario2.cleaned_data
            arriendo = Arriendos(nombre_pelicula=informacion2['nombre_pelicula'],fecha_arriendo=informacion2['fecha_arriendo'],cliente_arriendo=informacion2['cliente_arriendo'])
            arriendo.save()
            return render(request, 'inicio.html')
    else:
        miFormulario2 = ArriendoFormulario()

    return render(request, 'arriendoFormulario.html', {"miFormulario2": miFormulario2})

def busquedaArriendo(request):
    return render(request, 'busquedaArriendo.html') 

def buscar(request):
    if request.GET['nombre_pelicula']:
    #respuesta = f"Estoy buscando el arriendo de la pelicula: {request.GET['nombre_pelicula']}"
        nombre_pelicula = request.GET['nombre_pelicula']
        arriendos = Arriendos.objects.filter(nombre_pelicula__icontains=nombre_pelicula)

        return render(request, 'inicio.html', {'arriendos': arriendos, 'nombre pelicula': nombre_pelicula})

    else:
        respuesta = "No enviaste datos."
    
    return render(request, 'inicio.html', {'respuesta':respuesta})

