from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


# Proveedores

def muebles(request):
    return render(request, 'proveedores/muebles.html')

def articulos(request):
    return render(request, 'proveedores/articulos.html')

def madera(request):
    return render(request, 'proveedores/madera.html')