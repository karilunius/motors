from django.shortcuts import render, HttpResponse
from .models import Clientes
# Create your views here.
#@app.route('/ ')
def  inicio(request):
        #return HttpResponse('<h1>Pagina Principal</h1>')

        clientes = Clientes.objects.all()#se trae todos los registros de la tabla clientes
        print(clientes)#definir llave
        contexto = {
                'clientes' : clientes
        }
        return render(request, 'index.html', contexto)
#no funciono lo de ver el get 
