from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProdutoForm
from .models import Produto
from django.core.paginator import Paginator

def homepage(request):
    return render(request, 'loja_virtual_app/homepage.html')

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cadastro_sucesso')
    else:
        form = ProdutoForm()
    return render(request, 'loja_virtual_app/cadastrar_produto.html', {'form': form})

def cadastro_sucesso(request):
    return render(request, 'loja_virtual_app/cadastro_sucesso.html')

def listar_produtos(request):
    produtos_list = Produto.objects.all()
    paginator = Paginator(produtos_list, 9)  # 9 produtos por página
    page_number = request.GET.get('page')
    produtos = paginator.get_page(page_number)
    return render(request, 'loja_virtual_app/listar_produtos.html', {'produtos': produtos})

def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'loja_virtual_app/detalhe_produto.html', {'produto': produto})