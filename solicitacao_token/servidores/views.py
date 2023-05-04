from django.shortcuts import render, redirect
from .models import Servidor
from django.http import HttpResponse
from .form import ServidorForm
from django.contrib import messages
# Create your views here.

#faz a busca de todos os dados da tabela do banco
def listagem(request):
    data = {}
    data['servidor'] = Servidor.objects.all()  
    return render(request, 'servidores/listagem.html', data)

def cadastro_servidor(request):
    data = {}
    form = ServidorForm
    if request.method == 'POST':
        form = ServidorForm(request.POST, request.FILES)       
        if form.is_valid():
            form.save()
            messages.success(request,'Solicitação realizada com sucesso!')
            return redirect('cadastro_servidor')
    
    data['form'] = form
    return render(request, 'servidores/form.html', data)

def update(request, pk):
    data = {}
    cadastro_servidor = Servidor.objects.get(pk=pk)
    form = ServidorForm(request.POST or None, instance=cadastro_servidor)
    if form.is_valid():
            form.save()
            messages.success(request,'Alteração realizada')
            return redirect('listagem')
    data['form'] = form
    data['servidor'] = cadastro_servidor
    return render(request, 'servidores/form.html', data)

def delete(request, pk):
    solicitacao = Servidor.objects.get(pk=pk)
    solicitacao.delete()
    messages.success(request,'Exclusão realizada')
    return redirect('listagem')