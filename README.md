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
5. Execute as migrações para configurar o banco de dados:
    ```bash
    python manage.py migrate
6. Execute o servidor local:
    ```bash
    python manage.py runserver
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



