from multiprocessing import context
from django.shortcuts import render
from Familiares.models import familiar

def familia(request):
    familia = familiar.objects.all()
    context = {'familia':familia}
    return render(request, 'templates.html', context=context)