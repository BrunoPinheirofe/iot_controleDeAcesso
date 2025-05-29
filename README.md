# Projeto IoT - Controle de Acesso

Este projeto implementa um sistema de controle de acesso utilizando Django e Django REST framework, projetado para interagir com um dispositivo IoT (como um ESP32 com leitor RFID).

## Funcionalidades

*   API para verificar o acesso com base em um ID de cartão.
*   Registro de logs de tentativas de acesso.
*   Interface administrativa do Django para gerenciar usuários e logs de acesso.

## Configuração do Ambiente

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/BrunoPinheirofe/iot_controleDeAcesso
    cd iot_projeto
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    (Certifique-se de ter Django e djangorestframework instalados. Se você tiver um arquivo `requirements.txt`, use `pip install -r requirements.txt`)
    ```bash
    pip install Django djangorestframework
    ```

4.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Crie um superusuário para acessar o Django Admin:**
    ```bash
    python manage.py createsuperuser
    ```
    Siga as instruções para definir email, nome de usuário (opcional, se não estiver usando o `USERNAME_FIELD` padrão) e senha.

6.  **Execute o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```
    O servidor estará disponível em `http://127.0.0.1:8000/`.

## Uso da API

A API é o principal meio de interação para o dispositivo IoT.

### Verificar Acesso

*   **Endpoint:** `/verificar-acesso/`
*   **Método:** `POST`
*   **Corpo da Requisição (JSON):**
    ```json
    {
        "cardId": "SEU_CARD_ID_AQUI"
    }
    ```
*   **Respostas:**
    *   **Sucesso (Acesso Permitido - HTTP 200 OK):**
        ```json
        {
            "status": "Permitido",
            "message": "Acesso Permitido",
            "usuario": {
                "email": "usuario@exemplo.com",
                "cardId": "SEU_CARD_ID_AQUI"
                // Outros campos do UsuarioInfoSerializer
            }
        }
        ```
    *   **Falha (Acesso Negado - HTTP 403 FORBIDDEN):**
        ```json
        {
            "status": "Negado - Cartão desconhecido", // ou outra mensagem de negação
            "message": "Acesso Negado"
        }
        ```
    *   **Falha (Requisição Inválida - HTTP 400 BAD REQUEST):**
        ```json
        {
            "cardId": [
                "Este campo é obrigatório."
            ]
        }
        ```

## Uso do Django Admin

A interface administrativa do Django permite gerenciar os dados do sistema.

1.  **Acesse o Admin:**
    Navegue para `http://127.0.0.1:8000/admin/` no seu navegador.

2.  **Login:**
    Use as credenciais do superusuário criado durante a configuração.

3.  **Gerenciamento:**
    *   **Usuarios ([`gestao_acesso.Usuario`](gestao_acesso/models.py#L27)):**
        *   Você pode adicionar, modificar e excluir usuários.
        *   Ao adicionar ou modificar um usuário, certifique-se de preencher o campo `cardId` com o identificador RFID que será usado para o acesso.
        *   Outros campos como `email`, `is_active` (para ativar/desativar o acesso do usuário) e `is_staff` também podem ser gerenciados.
    *   **Log acess ([`gestao_acesso.LogAcess`](gestao_acesso/models.py#L45)):**
        *   Você pode visualizar os logs de todas as tentativas de acesso.
        *   Os logs incluem o `card_id` utilizado, o `timestamp` da tentativa e o `status` (Permitido/Negado).
        *   É possível filtrar e pesquisar os logs.

## Estrutura do Projeto

*   `core/`: Contém as configurações principais do projeto Django ([`core/settings.py`](core/settings.py), [`core/urls.py`](core/urls.py)).
*   `gestao_acesso/`: Aplicação Django responsável pela lógica de controle de acesso.
    *   [`gestao_acesso/models.py`](gestao_acesso/models.py): Define os modelos de dados (`Usuario`, `LogAcess`).
    *   [`gestao_acesso/views.py`](gestao_acesso/views.py): Contém a lógica das views da API (ex: [`VerificarAcessoView`](gestao_acesso/views.py#L8)).
    *   [`gestao_acesso/serializers.py`](gestao_acesso/serializers.py): Define como os dados são convertidos para JSON e validados.
    *   [`gestao_acesso/urls.py`](gestao_acesso/urls.py): Define as URLs específicas da aplicação `gestao_acesso`.
    *   [`gestao_acesso/admin.py`](gestao_acesso/admin.py): Configura a interface administrativa para os modelos da aplicação.
*   [`manage.py`](manage.py): Utilitário de linha de comando do Django.
*   [`db.sqlite3`](db.sqlite3): Banco de dados SQLite padrão (para desenvolvimento).

## Próximos Passos / Melhorias (Sugestões)

*   Implementar autenticação para endpoints de gerenciamento de usuários via API (se necessário).
*   Adicionar mais testes unitários e de integração.
*   Configurar para produção (ex: usando Gunicorn, Nginx, PostgreSQL).
*   Melhorar a segurança (ex: HTTPS, tratamento de segredos).
```// filepath: README.md
# Projeto IoT - Controle de Acesso

Este projeto implementa um sistema de controle de acesso utilizando Django e Django REST framework, projetado para interagir com um dispositivo IoT (como um ESP32 com leitor RFID).

## Funcionalidades

*   API para verificar o acesso com base em um ID de cartão.
*   Registro de logs de tentativas de acesso.
*   Interface administrativa do Django para gerenciar usuários e logs de acesso.

## Configuração do Ambiente

1.  **Clone o repositório:**
    ```bash
    git clone <url-do-seu-repositorio>
    cd iot_projeto
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    (Certifique-se de ter Django e djangorestframework instalados. Se você tiver um arquivo `requirements.txt`, use `pip install -r requirements.txt`)
    ```bash
    pip install Django djangorestframework
    ```

4.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Crie um superusuário para acessar o Django Admin:**
    ```bash
    python manage.py createsuperuser
    ```
    Siga as instruções para definir email, nome de usuário (opcional, se não estiver usando o `USERNAME_FIELD` padrão) e senha.

6.  **Execute o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```
    O servidor estará disponível em `http://127.0.0.1:8000/`.

## Uso da API

A API é o principal meio de interação para o dispositivo IoT.

### Verificar Acesso

*   **Endpoint:** `/verificar-acesso/`
*   **Método:** `POST`
*   **Corpo da Requisição (JSON):**
    ```json
    {
        "cardId": "SEU_CARD_ID_AQUI"
    }
    ```
*   **Respostas:**
    *   **Sucesso (Acesso Permitido - HTTP 200 OK):**
        ```json
        {
            "status": "Permitido",
            "message": "Acesso Permitido",
            "usuario": {
                "email": "usuario@exemplo.com",
                "cardId": "SEU_CARD_ID_AQUI"
                // Outros campos do UsuarioInfoSerializer
            }
        }
        ```
    *   **Falha (Acesso Negado - HTTP 403 FORBIDDEN):**
        ```json
        {
            "status": "Negado - Cartão desconhecido", // ou outra mensagem de negação
            "message": "Acesso Negado"
        }
        ```
    *   **Falha (Requisição Inválida - HTTP 400 BAD REQUEST):**
        ```json
        {
            "cardId": [
                "Este campo é obrigatório."
            ]
        }
        ```

## Uso do Django Admin

A interface administrativa do Django permite gerenciar os dados do sistema.

1.  **Acesse o Admin:**
    Navegue para `http://127.0.0.1:8000/admin/` no seu navegador.

2.  **Login:**
    Use as credenciais do superusuário criado durante a configuração.

3.  **Gerenciamento:**
    *   **Usuarios ([`gestao_acesso.Usuario`](gestao_acesso/models.py#L27)):**
        *   Você pode adicionar, modificar e excluir usuários.
        *   Ao adicionar ou modificar um usuário, certifique-se de preencher o campo `cardId` com o identificador RFID que será usado para o acesso.
        *   Outros campos como `email`, `is_active` (para ativar/desativar o acesso do usuário) e `is_staff` também podem ser gerenciados.
    *   **Log acess ([`gestao_acesso.LogAcess`](gestao_acesso/models.py#L45)):**
        *   Você pode visualizar os logs de todas as tentativas de acesso.
        *   Os logs incluem o `card_id` utilizado, o `timestamp` da tentativa e o `status` (Permitido/Negado).
        *   É possível filtrar e pesquisar os logs.

## Estrutura do Projeto

*   `core/`: Contém as configurações principais do projeto Django ([`core/settings.py`](core/settings.py), [`core/urls.py`](core/urls.py)).
*   `gestao_acesso/`: Aplicação Django responsável pela lógica de controle de acesso.
    *   [`gestao_acesso/models.py`](gestao_acesso/models.py): Define os modelos de dados (`Usuario`, `LogAcess`).
    *   [`gestao_acesso/views.py`](gestao_acesso/views.py): Contém a lógica das views da API (ex: [`VerificarAcessoView`](gestao_acesso/views.py#L8)).
    *   [`gestao_acesso/serializers.py`](gestao_acesso/serializers.py): Define como os dados são convertidos para JSON e validados.
    *   [`gestao_acesso/urls.py`](gestao_acesso/urls.py): Define as URLs específicas da aplicação `gestao_acesso`.
    *   [`gestao_acesso/admin.py`](gestao_acesso/admin.py): Configura a interface administrativa para os modelos da aplicação.
*   [`manage.py`](manage.py): Utilitário de linha de comando do Django.
*   [`db.sqlite3`](db.sqlite3): Banco de dados SQLite padrão (para desenvolvimento).

## Próximos Passos / Melhorias (Sugestões)

*   Implementar autenticação para endpoints de gerenciamento de usuários via API (se necessário).
*   Adicionar mais testes unitários e de integração.
*   Configurar para produção (ex: usando Gunicorn, Nginx, PostgreSQL).
*   Melhorar a segurança (ex: HTTPS, tratamento de segredos).