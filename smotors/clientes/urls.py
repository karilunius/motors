
from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crearCliente/', views.crearCliente, name='crearCliente'),
]
#esta ruta , el nombre se puede conectar al navbar mediante el nombre
