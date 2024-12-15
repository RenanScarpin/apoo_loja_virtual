from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProdutoForm
from .models import Produto
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignupForm  # Certifique-se de que o formulário está importado
from .forms import LoginForm

# Função para a página inicial do site
def homepage(request):
    return render(request, 'loja_virtual_app/homepage.html')

# Função para cadastrar novo produto no sistema
@login_required
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)  # Não salva ainda no banco
            produto.usuario = request.user  # Associa o produto ao usuário logado
            produto.save()
            return redirect('cadastro_sucesso')
    else:
        form = ProdutoForm()
    return render(request, 'loja_virtual_app/cadastrar_produto.html', {'form': form})


# Página estática de confirmação após o cadastro de um produto
@login_required
def cadastro_sucesso(request):
    return render(request, 'loja_virtual_app/cadastro_sucesso.html')

# Função para exibir uma lista paginada de produtos cadastrados
@login_required
def listar_produtos(request):
    produtos_list = Produto.objects.filter(usuario=request.user)  # Filtra produtos do usuário logado
    paginator = Paginator(produtos_list, 9)
    page_number = request.GET.get('page')
    produtos = paginator.get_page(page_number)
    return render(request, 'loja_virtual_app/listar_produtos.html', {'produtos': produtos})


# Função para exibir os detalhes de um produto
@login_required
def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'loja_virtual_app/detalhe_produto.html', {'produto': produto})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('homepage')
        else:
            messages.error(request, 'Credenciais inválidas.')

    # Pega apenas a última mensagem
    last_message = ''
    storage = messages.get_messages(request)
    for message in storage:
        last_message = message  # Sobrescreve para pegar a última mensagem

    return render(request, 'loja_virtual_app/login.html', {'form': form, 'last_message': last_message})


# Função para logout de usuários
def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu da sua conta.')
    return redirect('login')

# Função para cadastro de novos usuários
def signup(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        User.objects.create_user(username=username, password=password)
        messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
        return redirect('login')
    return render(request, 'loja_virtual_app/signup.html', {'form': form})