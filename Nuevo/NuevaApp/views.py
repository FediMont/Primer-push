from multiprocessing import context
from django.shortcuts import render
from NuevaApp.models import Bibliotecas
from NuevaApp.forms import Biblio_form

# Create your views here.
def index(request):
    return render(request,'index.html',)

def bibliotecas(request):
    return render(request,'bibliotecas.html')

def biblio_list(request):
    bibliotecas = Bibliotecas.objects.all()
    context = {'bibliotecas':bibliotecas}
    return render(request,'biblio_list.html', context=context)

def carga_biblio(request):
    if request.method == 'GET':
        form = Biblio_form()
        context = {'form':form}
        return render(request,'carga_biblio.html', context=context)
    else:
        form = Biblio_form(request.POST)
        if form.is_valid():
            nueva_biblio = Bibliotecas.objects.create(
                nombre = form.cleaned_data['nombre'],
                provincia = form.cleaned_data['provincia'],
                localidad = form.cleaned_data['localidad'],
                direccion = form.cleaned_data['direccion'],
                apertura = form.cleaned_data['apertura'],
                link = form.cleaned_data['link'],
                imagen = form.cleaned_data['imagen'],
                )   
            context={'nueva_biblio':nueva_biblio}
        return render(request,'carga_biblio.html', context=context)


def busca_biblio(request):
    biblioteca = Bibliotecas.objects.filter(nombre__icontains = request.GET['search'])
    context = {'biblioteca':biblioteca}
    return render(request,'busca_biblio.html', context=context)