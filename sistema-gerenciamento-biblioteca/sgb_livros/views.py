from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Livro
from django.contrib.auth.decorators import login_required

# Create your views here.
def livros(request):
    #return HttpResponse('Olá mundo')
    return render(request, 'livros.html')

def salva_livros(request):
    titulo_livro = request.POST['titulo_livro']
    autor_livro = request.POST['autor_livro']
    editora_livro = request.POST['editora_livro']
    return render(request, 'livros.html', context = {'titulo_livro': titulo_livro})
    #return HttpResponse('Livro salvo!' + titulo_livro)

@login_required
def cadastra_livro(request):
    if request.method == 'POST':
        livro_id = request.POST['livro_id']
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        ano_publicacao = request.POST['ano_publicacao']
        editora = request.POST['editora']

        if livro_id:        # Edita livro
            livro = livro_id
            livro.titulo = titulo
            livro.autor = autor
            livro.ano_publicacao = ano_publicacao
            livro.editora = editora
            livro.save()
        else:       # Salva um novo livro
            Livro.objects.create(
                titulo = titulo,
                autor = autor,
                ano_publicacao = ano_publicacao,
                editora = editora
            )
        return redirect('cadastra_livro')
    # objects é o gerenciador do Django que serve para consultar o banco.
    # all() é uma função que retorna todos os registros da tabela livro. (mesma coisa que o SELECT em Banco de Dados).
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros': livros})

@login_required
def exclui_livro(request, livro_id):
    # get_object_or_404() esta função busca no banco de dados um objeto da tabela Livro cujo campo id seja igual a livro_id. Se encontrar, retorna o objeto e guarda na variável livro. Se não encontrar, retorna uma página 404.
    livro = get_object_or_404(Livro, id=livro_id)
    livro.delete()
    return redirect('cadastra_livro')

@login_required
def edita_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    livros = Livro.objects.all()

    if request.method == "POST":
        livro.titulo = request.POST['titulo']
        livro.autor = request.POST['autor']
        livro.ano_publicacao = request.POST['ano_publicacao']
        livro.editora = request.POST['editora']
        livro.save()
        return redirect('cadastra_livro')
    
    return render(request, 'livros.html', {'livros': livros, 'livro_editar': livro})
