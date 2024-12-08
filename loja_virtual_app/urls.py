from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Homepage na raiz do app
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('sucesso/', views.cadastro_sucesso, name='cadastro_sucesso'),
    path('listar/', views.listar_produtos, name='listar_produtos'),
    path('detalhe/<int:produto_id>/', views.detalhe_produto, name='detalhe_produto'),
]
