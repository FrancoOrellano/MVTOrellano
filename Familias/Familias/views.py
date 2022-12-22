from django.http import HttpResponse
from Familiares.models import Familiar
from django.shortcuts import render

def familiar(request):
    familiar = Familiar(nombre='Julio Maximo Orellano', parentesco='Padre', edad=60, esta_vivo= False)
    familiar.save()
    documento_de_texto = f'Nombre= {familiar.nombre}\n Parentesco= {familiar.parentesco}\n Edad= {familiar.edad}\n Esta vivo? {familiar.esta_vivo}'
    return HttpResponse(documento_de_texto)

def lista_familiares(request):
    lista = Familiar.objects.all()
    context = {
        'familiar': lista,
    }
    return render(request, 'templates.html', context=context)