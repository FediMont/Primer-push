from django.shortcuts import render
from App1.models import Products


# Create your views here.
def products(request):
    producto_nuevo = Products.objects.create(
        name = 'Panchito', 
        price = 100,
        description = "Con papita como el cumpleanito'", 
        SKU = 'JPCASD1231245'
        )
    context = {'producto_nuevo':producto_nuevo}
    return render(request, 'products.html', context=context)