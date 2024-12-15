from django.urls import path
from . import views

urlpatterns = [
    # Páginas relacionadas a produtos
    path('', views.homepage, name='homepage'),  # Homepage na raiz do app
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('sucesso/', views.cadastro_sucesso, name='cadastro_sucesso'),
    path('listar/', views.listar_produtos, name='listar_produtos'),
    path('detalhe/<int:produto_id>/', views.detalhe_produto, name='detalhe_produto'),

    # Páginas relacionadas a autenticação
    path('login/', views.login_view, name='login'),  # Página de login
    path('logout/', views.logout_view, name='logout'),  # Página de logout
    path('signup/', views.signup, name='signup'),  # Página de cadastro
]
