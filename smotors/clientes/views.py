from django.shortcuts import render, HttpResponse
from .models import Clientes
# Create your views here.
#@app.route('/ ')


def crearCliente(request) :
        return render(request, 'crearCliente.html')


def contactenos(request) :
        return render(request, 'contactenos.html')


def inicio(request) :
        return render(request, 'index.html')

def  clientes(request):
        #return HttpResponse('<h1>Pagina Principal</h1>')

        clientes = Clientes.objects.all()#se trae todos los registros de la tabla clientes
        print(clientes)#definir llave
        contexto = {
                'clientes' : clientes
        }
        return render(request, 'clientes.html', contexto)
#no funciono lo de ver el get  luego de reiniciar sí funcionó