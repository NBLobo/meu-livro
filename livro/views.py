from django.shortcuts import render, redirect, HttpResponse
from .models import Livro
from .forms import LivroForm


def livro(request):
    dados = {
        'dados': Livro.objects.all()
    }
    return render(request, 'livro/livro.html', context=dados)


def detalhe(request, id_livro):
    dados = {
        'dados': Livro.objects.get(pk=id_livro)
    }
    return render(request, 'livro/detalhe.html', dados)


def criar(request):
    if request.method == 'POST':
        livro_form = LivroForm(request.POST)
        if livro_form.is_valid():
            livro_form.save()
        return redirect('livro')
    else:
        livro_form = LivroForm()
        formulario = {'formulario': livro_form}
        return render(request, 'livro/novo_livro.html', context=formulario)


def editar(request, id_livro):
    livro = Livro.objects.get(pk=id_livro)
    if request.method == 'GET':
        formulario = LivroForm(instance=livro)
        return render(request, 'livro/novo_livro.html', {'formulario': formulario})
    else:
        formulario = LivroForm(request.POST, instance=livro)
        if formulario.is_valid():
            formulario.save()
        return redirect('livro')


def excluir(request, id_livro):
    livro = Livro.objects.get(pk=id_livro)
    if request.method == 'POST':
        livro.delete()
        return redirect('livro')
    return render(request, 'livro/confirmar_exclusao.html', {'item': livro})
