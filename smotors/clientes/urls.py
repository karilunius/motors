
from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crearCliente/', views.crearCliente, name='crearCliente'),
    path('contactenos/', views.contactenos, name='contactenos'),
    path('clientes/', views.clientes, name='clientes'),
]
#esta ruta , el nombre se puede conectar al navbar mediante el nombre
