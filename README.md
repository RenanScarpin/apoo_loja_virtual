Como testar o site utilizando o vscode:

No linux:
source .venv/bin/activate

No Windows:
Execute no terminal do vscode:
.venv\Scripts\activate.bat


Então, no VScode aperte ctrl+shift+p e selecione
Python: Select interpreter
E selecione .venv
Então abra um terminal no vscode que seja cmd (commandprompt) e não powershell e execute
python manage.py runserver

Em ambos os casos, o site estará disponível no localhost na porta 8000
No navegador pode ser acessado digitando a URL:
127.0.0.1:8000

Importante para desenvolvimento
Para adaptar a base de dados as mudanças no código, execute os comandos:
python manage.py makemigrations
python manage.py migrate
