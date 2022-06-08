from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def saludo(request, nombre):
    return HttpResponse(f'Hello {nombre}!! :D')

def despedida(request):
    return HttpResponse('Byebye World!!')

def fecha_actual(request):
    fecha = datetime.now().strftime('%d/%m/%Y')
    mensaje = f'Hoy es {fecha}!!'
    return HttpResponse(mensaje)

def probando_template(request):
    context = {
        'nombre':'Federico',
        'apellido':'Montagna',
        'frutas':['banana','manzana','pera'],
        'fecha':datetime.now(),
        'edades':[18,29,5,10,12,17,22,40]
    }
    return render(request,'template1.html', context = context)