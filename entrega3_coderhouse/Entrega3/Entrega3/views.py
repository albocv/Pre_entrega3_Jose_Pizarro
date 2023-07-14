#from contextvars import Context
import datetime
from django.http import HttpResponse
from django.template import Template,Context 
from django.template import loader

def saludo(request):
    return HttpResponse("Hola Django-Coder")

def segunda_vista(request):
    return HttpResponse("<br></br>Esto es muy simple")

def diaDeHoy(request):

    dia = datetime.datetime.now()

    documentoDeTexto = f"Hoy es dia: <br> {dia}"

    return HttpResponse(documentoDeTexto)

def miNombreEs(self,nombre):
    
    documentoDeTexto = f"Mi nombre es: <br></br>   {nombre}"

    return HttpResponse(documentoDeTexto)

def probandoTemplate(self):
    
    nom = 'Jose'
    ape = 'Pizarro'

    lista_notas = [2,2,3,7,2,5]

    diccionario = {'nombre': nom, 'apellido': ape, 'hoy': datetime.datetime.now(), 'notas': lista_notas}
    

    #miHtml = open('C:/Users/admin/MisArchivosPython/entrega3_coderhouse/Entrega3/Entrega3/plantillas/template1.html')

    #plantilla = Template(miHtml.read()) 

    #miHtml.close()

    #miContexto = Context()

    #documento = plantilla.render(miContexto)

    plantilla = loader.get_template('template1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
