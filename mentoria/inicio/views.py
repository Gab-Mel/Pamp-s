from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse 
from django.urls import reverse_lazy

from inicio.forms import novo_user, nova_pendencia

# Create your views here.

def special(request):
    return render(request, 'inicio/index.htm')

def aluno(request):
    if request.method == 'POST':
        form = novo_user(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'inicio/index.htm')
        else:
            render(request, 'inicio/create.htm', {'form':form}, status=400)

def pendencia(request):
    if request.method == 'POST':
        pet = nova_pendencia(request.POST)
        if pet.is_valid():
            pet.save()


            return render(request, 'inicio/usuario/agenda.htm')


        else:
            render(request, 'inicio/usuario/agenda.htm', {'pet':pet}, status=400)
    
def navegar(request, chave):
    if chave == 'criar':
        return render(request, 'inicio/create.htm')
    elif chave == 'usuario':
        return render(request, 'inicio/usuario.htm')

def viajar(request, chave):
    if chave == 'agenda':
        return render(request, 'inicio/usuario/agenda.htm')
    elif chave == 'material':
        return render(request, 'inicio/usuario/material.htm')
    elif chave == 'mural':
        return render(request, 'inicio/usuario/mural.htm')
    elif chave == 'video':
        return render(request, 'inicio/usuario/video.htm')
 


#def paisagem(request):
#    if request.method == 'POST':
#        if request.method == 'POST':
#            farm = fotofx(request.POST, request.FILES)
#            if farm.is_volid():
#                farm.save()
#                return redirect(reverse_lazy("inicio:special"))
#        else:
#            farm = fotofx()
#        context = {
#            'farm': farm
#        }
#        return render(request, 'inicio/paisagem.html')

