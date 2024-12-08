Como testar o site:

No linux:
source .venv/bin/activate
python manage.py runserver

No Windows:
.venv\Scripts\Ativar.ps1
python manage.py runserver

Em ambos os casos, o site estará disponível no localhost na porta 8000
No navegador pode ser acessado digitando a URL:
127.0.0.1:8000

Importante para desenvolvimento
Para adaptar a base de dados as mudanças no código, execute os comandos:
python manage.py makemigrations
python manage.py migrate
