from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProdutoForm
from .models import Produto
from django.core.paginator import Paginator

#Função para a página inicial do site, o render combina o template de homepage.html, que está na pasta de templates
#com dados opcionais para gerar a resposta HTTP que será enviada ao navegador
def homepage(request):
    return render(request, 'loja_virtual_app/homepage.html')

#Função para cadastrar novo produto no sistema
def cadastrar_produto(request):
    if request.method == 'POST': #Request é usado para checar se a submissão é do tipo POST (submissão de formulário) ou do tipo GET (carregamento inicial de página)
        form = ProdutoForm(request.POST, request.FILES)#Cria um formulário ProdutoForm com os dados enviados (request.POST) e os arquivos anexados (request.FILES).
        if form.is_valid():# Se o formulário estiver válido, salva os dados no banco de dados
            form.save()
            return redirect('cadastro_sucesso')
    else:# Se a submissão for do tipo GET, Cria um formulário vazio para exibir ao usuário.
        form = ProdutoForm()
    return render(request, 'loja_virtual_app/cadastrar_produto.html', {'form': form})

#Apenas renderiza a página estática de confirmação após o cadastro de um produto, usando o template de cadastro_sucesso.html
def cadastro_sucesso(request):
    return render(request, 'loja_virtual_app/cadastro_sucesso.html')

#Função para exibir uma lista paginada de produtos cadastrados
def listar_produtos(request):
    produtos_list = Produto.objects.all()#Recupera todos os produtos do banco de dados
    paginator = Paginator(produtos_list, 9)  # Divide a lista de produtos em páginas com 9 produtos por página
    page_number = request.GET.get('page') # Obtém o número da página
    produtos = paginator.get_page(page_number) # Recupera os produtos da página atual
    return render(request, 'loja_virtual_app/listar_produtos.html', {'produtos': produtos})

# Renderiza a página estática que exibe os detalhes do produto
def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id) # Usa get_object_or_404 para buscar o produto com o ID fornecido no banco de dados, se o produto não existir, retorna uma página de erro 404
    return render(request, 'loja_virtual_app/detalhe_produto.html', {'produto': produto})
