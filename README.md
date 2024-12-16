# Loja Virtual
Este é um projeto Django para gerenciamento de produtos com funcionalidades de autenticação de usuários (cadastro, login, logout). O projeto permite adicionar, listar e visualizar detalhes de produtos.

# Requisitos
Antes de começar, certifique-se de ter os seguintes itens instalados no seu computador:

- Python 3.8+
- Git
- Virtualenv (opcional, mas recomendado)
# Como Rodar o Projeto
1. Clone o Repositório
```
git clone https://github.com/RenanScarpin/apoo_loja_virtual.git
```
2. Navegue até a pasta do projeto
```
cd apoo_loja_virtual
```
3. Crie e Ative um Ambiente Virtual
No Windows:
```
python -m venv venv
venv\Scripts\activate
```
No macOS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```
4. Instale as Dependências
Certifique-se de estar no diretório raiz do projeto e execute:

```
pip install -r requirements.txt
```
5. Prepare o Banco de Dados
Execute as migrações para configurar o banco de dados:

```
python manage.py makemigrations
python manage.py migrate
```
6. Inicie o Servidor Local
Para rodar o projeto localmente, execute:

```
python manage.py runserver
```
Acesse o projeto no navegador em: http://127.0.0.1:8000/

Funcionalidades
- Cadastro de Usuário: Página para novos usuários se cadastrarem.
- Login e Logout: Permite que usuários façam login e logout.
- Gerenciamento de Produtos: Adicione, liste e visualize detalhes de produtos.
- Autenticação: Apenas usuários autenticados podem gerenciar produtos.
