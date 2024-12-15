Loja Virtual
Este é um projeto Django para gerenciamento de produtos com funcionalidades de autenticação de usuários (cadastro, login, logout). O projeto permite adicionar, listar e visualizar detalhes de produtos.

Requisitos
Antes de começar, certifique-se de ter os seguintes itens instalados no seu computador:

Python 3.8+ (Download aqui)
Git (Download aqui)
Virtualenv (opcional, mas recomendado)
Como Rodar o Projeto
1. Clone o Repositório
bash
Copiar código
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
2. Crie e Ative um Ambiente Virtual
No Windows:
bash
Copiar código
python -m venv venv
venv\Scripts\activate
No macOS/Linux:
bash
Copiar código
python3 -m venv venv
source venv/bin/activate
3. Instale as Dependências
Certifique-se de estar no diretório raiz do projeto e execute:

bash
Copiar código
pip install -r requirements.txt
4. Configure as Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto e adicione as seguintes configurações:

makefile
Copiar código
SECRET_KEY=coloque-sua-secret-key-aqui
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
Se necessário, adicione outras variáveis específicas para o seu projeto.

5. Prepare o Banco de Dados
Rode as migrações do banco de dados:

bash
Copiar código
python manage.py migrate
6. Inicie o Servidor Local
Para rodar o projeto localmente, execute:

bash
Copiar código
python manage.py runserver
Acesse o projeto no navegador em: http://127.0.0.1:8000/

Funcionalidades
Cadastro de Usuário: Página para novos usuários se cadastrarem.
Login/Logout: Permite que usuários façam login e logout.
Gerenciamento de Produtos: Adicione, liste e visualize detalhes de produtos.
Autenticação: Apenas usuários autenticados podem gerenciar produtos.
