from django import forms

class ClienteFormulario(forms.Form):
    nombre_cliente = forms.CharField()
    apellido_cliente = forms.CharField()
    direccion_cliente = forms.CharField()

class ArriendoFormulario(forms.Form):
    nombre_pelicula = forms.CharField()
    fecha_arriendo = forms.CharField()
    cliente_arriendo = forms.CharField()    