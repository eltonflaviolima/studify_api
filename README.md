# Flashcards API

Este projeto é uma API para um web app de flashcards de estudo, desenvolvido com **Django** e **Django Rest Framework**. Ele permite que os usuários gerenciem disciplinas, decks, e flashcards para melhorar seus estudos e monitorar o progresso.

## Tecnologias Utilizadas
- **Python 3.8+**
- **Django 3.2+**
- **Django Rest Framework**
- **SQLite (ou outro banco de dados à sua escolha)**
- **Bootstrap 5 (para a interface web)**

## Funcionalidades

1. **Gerenciamento de Disciplinas**  
   - CRUD para as disciplinas, permitindo criar, visualizar, atualizar e deletar disciplinas de estudo.
   - Cada disciplina é vinculada a um usuário específico.

2. **Gerenciamento de Decks**
   - CRUD para decks, organizados por disciplina.
   - Nível de conhecimento é atribuído a cada deck, de 0 a 4.
   
3. **Gerenciamento de Flashcards**
   - CRUD para flashcards.
   - Nível de conhecimento é atribuído a cada flashcard, de 0 a 4.
   - Cada flashcard pertence a um deck específico.

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
2. Navegue até o diretório do projeto:
    ```bash
    cd studify_api
3. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate      # Para Windows
4. Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt
5. Crie um arquivo python e gere uma nova chave de secreta do Django:
    ```python
    from django.core.management.utils import get_random_secret_key; 
    print(get_random_secret_key())
6. Crie um arquivo `.env` e salve a `SECRET_KEY`:
    ```bash
    SECRET_KEY='<CHAVE_GERADA_NO_PASSO_5>'
7. Execute as migrações para configurar o banco de dados:
    ```bash
    python manage.py migrate
8. Execute o servidor local:
    ```bash
    python manage.py runserver
9. Crie um super usuário para administrar o banco local
    ```bash
    python manage.py createsuperuser
## Autenticação
A etapa de autenticação com o django rest-framework pode ser feito utilizando um token por usuário cadastrado.<br>
O DRF tem o módulo `rest_framework.authtoken` que auxilia na hora de implementar autenticação para a nossa api.<br>
Uma vez implementado esse módulo é possível utilizar o comando abaixo para obter um token para um usuário especificado:
```bash
python manage.py drf_create_token "nome_do_usuario"
```
Depois de gerar o token, abra o arquivo `authentication_token.py` na pasta playground e cole o token no lugar de `<TOKEN GERADO>`<br><br>
No entanto, a principal forma de autenticação é através da chamada: 
```bash
POST http://127.0.0.1:8000/api/auth/login/

body: 
{
    'username':'<NOME_DO_USUARIO>';
    'password':'<SENHA>';
}
```
Dessa forma se obterá o token de autenticação. <br>
[Referência 1](https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html)<br>
[Referência 2](https://dev.to/romeopeter/django-rest-framework-tokenauthentication-1544)
## Endpoints Principais

### 1. Disciplinas

| Método  | Endpoint                 | Descrição                   |
|---------|--------------------------|-----------------------------|
| GET     | `/api/disciplinas/`       | Lista todas as disciplinas   |
| POST    | `/api/disciplinas/`       | Cria uma nova disciplina     |
| GET     | `/api/disciplinas/{id}/`  | Detalha uma disciplina       |
| PUT     | `/api/disciplinas/{id}/`  | Atualiza uma disciplina      |
| DELETE  | `/api/disciplinas/{id}/`  | Exclui uma disciplina        |

### 2. Decks

| Método  | Endpoint             | Descrição                     |
|---------|----------------------|-------------------------------|
| GET     | `/api/decks/`         | Lista todos os decks          |
| POST    | `/api/decks/`         | Cria um novo deck             |
| GET     | `/api/decks/{id}/`    | Detalha um deck específico     |
| PUT     | `/api/decks/{id}/`    | Atualiza um deck específico    |
| DELETE  | `/api/decks/{id}/`    | Exclui um deck específico      |

### 3. Flashcards

| Método  | Endpoint               | Descrição                       |
|---------|------------------------|---------------------------------|
| GET     | `/api/flashcards/`      | Lista todos os flashcards       |
| POST    | `/api/flashcards/`      | Cria um novo flashcard          |
| GET     | `/api/flashcards/{id}/` | Detalha um flashcard específico |
| PUT     | `/api/flashcards/{id}/` | Atualiza um flashcard específico|
| DELETE  | `/api/flashcards/{id}/` | Exclui um flashcard específico  |



