from django.shortcuts import render, redirect
from .models import crud2
from .forms import crud2Form

def index (request):  # lee los archivos.html
    index2 = crud2.objects.all()
    return render(request,'static/index.html', {'index2': index2})

def crear (request):
    formulario =crud2Form(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request,'static/crear.html', {'formulario': formulario})


def leer (request):
    return render(request,'static/leer.html')


def actualizar (request, id):
    index2 = crud2.objects.get(id=id)
    formulario =crud2Form(request.POST or None, request.FILES or None, instance=index2)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('index')
    return render(request,'static/actualizar.html', {'formulario': formulario})


def borrar (request, id):
    index = crud2.objects.get(id=id)
    index.delete()
    return redirect('index')


def contacto (request):
    return render(request,'static/contacto.html')
def formulario (request):
    return render(request,'static/formulario.html')
