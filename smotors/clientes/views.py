from django.shortcuts import render, HttpResponse

# Create your views here.
#@app.route('/ ')
def  inicio(request):
        #return HttpResponse('<h1>Pagina Principal</h1>')
        return render(request, 'index.html')

