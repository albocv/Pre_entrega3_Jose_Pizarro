from django.urls import path
from AppEntrega3 import views


urlpatterns = [
    path('',views.inicio, name='Inicio'),
    path('clientes', views.vistaClientes, name='Clientes'),
    path('peliculas', views.vistaPeliculas, name='Peliculas'),
    path('arriendos', views.vistaArriendos, name='Arriendos'),
    path('clienteFormulario', views.clienteFormulario, name='ClienteFormulario'),
    path('arriendoFormulario', views.arriendoFormulario, name='ArriendoFormulario'),
    path('busquedaArriendo', views.busquedaArriendo, name='BusquedaArriendo'),
    path('buscar/', views.buscar),
]