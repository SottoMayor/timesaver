# Sistema de Agendamento — Flask + Jinja + SQLAlchemy

## Como rodar o app Dockerizado

Na raiz do projeto, execute:

```
docker-compose up
```

Depois, acesse:

```
http://localhost:5000/schedules
```

O app roda as migrations automaticamente, isso está embutido no `CMD` do Dockerfile.

## Como rodar o projeto localmente (fora do Docker)

1. Instale os requirements:

```
pip install -r requirements.txt
```
- Na seção "**Configuração do Projeto** > **1. Ambiente virtual (venv) e inicialização com Flask**" está descrito como rodar o venv.

2. Certifique que as migrations estão levantadas:

```
flask db upgrade -d database/migrations
```

3. Rode o server de desenvolvimento:
```
flask run
```

4. Acesse:
```
http://localhost:5000/schedules
```
   
---

## Entidade `Schedule`

| Campo             | Tipo    | Restrições   |
|------------------|---------|--------------|
| `id`             | int     | Primary Key  |
| `schedule_date`  | date    | Not Null     |
| `schedule_time`  | string  | Not Null     |
| `client`         | string  | Not Null     |
| `tuss_code`      | string  | Not Null     |
| `tuss_description`| string | Not Null     |
| `agreement`      | string  | Nullable     |

---

## Endpoints disponíveis

### [GET] `/schedules`
Lista todos os agendamentos, com suporte a filtros opcionais via query string:

```
/schedules?date={schedule_date}&client={client}&service={tuss_description}
```

### [GET] `/schedules/create`
Renderiza o formulário para criar um novo agendamento.

### [POST] `/schedules`
Cria um novo agendamento com base nos dados do formulário.

**Body esperado:**

```
{
  "cliente": string,
  "tuss_codigo": string,
  "data": string,
  "horario": string,
  "convenio": string | ""
}
```

### [GET] `/schedules/update/<id>`
Carrega o formulário preenchido para editar um agendamento existente.

### [POST] `/schedules/update/<id>`
Atualiza os dados de um agendamento.

**Body esperado:**

```
{
  "cliente": string,
  "tuss_codigo": string,
  "data": string,
  "horario": string,
  "convenio": string | ""
}
```

### [POST] `/schedules/delete/<id>`
Remove o agendamento com o ID informado.

## Observações sobre o uso de Jinja (Template Engine)

> Como este projeto utiliza Jinja para renderizar os templates HTML:

1. Só existem métodos `GET` e `POST` nas rotas — não há uso de `PATCH` ou `DELETE` diretamente no navegador.
2. Todos os dados enviados pelo `body` (formulários) chegam como **string**.
---

## Configuração do Projeto

### 1. Ambiente virtual (venv) e inicialização com Flask

- O projeto utiliza `venv` para isolamento do ambiente Python.
- Instruções para ativar/desativar (só use se for mexer no projeto como desenvolvedor):

**Windows:**
```
venv\Scripts\activate
```

**Linux/macOS:**
```
source venv/bin/activate
```

Para iniciar a aplicação localmente:
```
flask run
```


### 2. Variáveis de ambiente (python-dotenv)

- As variáveis são carregadas automaticamente com `python-dotenv`.

**Arquivos envolvidos:**

- `settings/env.py` -> Importa as variáveis para uso no app Flask.
- `.env` -> Define variáveis de ambiente da aplicação.
- `.flaskenv` -> Define variáveis necessárias para rodar o `flask run`.


### 3. Conexão com o banco de dados

- ORM: `SQLAlchemy`
- SGBD: `SQLite`

**Estrutura de código:**

- `database/connection.py` -> Instância global do `SQLAlchemy`
- `models/` -> Entidades da aplicação (ex: `ScheduleModel`)


### 4. Migrations (Flask-Migrate)

- O projeto utiliza `Flask-Migrate` para versionamento e aplicação de migrations.

- `database/migrations/` -> Localização das Migrations


### 5. Blueprints e Validação (Flask-Smorest + Marshmallow)

- `resources/` -> Blueprints das rotas do app.
- `schemas/` -> Schemas de validação de dados com `Marshmallow`.

### 6. Template engine (Jinja)
- `templates/` -> Templates HTML renderizados com Jinja
- `static/` -> arquivos estáticos (CSS)

### 7. Dockerização

- **Dockerfile (dev)**:
  - Não usa multi-stage.
  - Roda sem WSGI (apenas `flask run`).
  - Foco em desenvolvimento e iteração rápida.

- **docker-compose**:
  - Sobe o app flask dockerizado 

### 8. Estrutura de pastas:

```
├── .env
├── .flaskenv
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
├── app.py
├── database
    ├── connection.py
    └── migrations
    │   ├── README
    │   ├── alembic.ini
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions
    │       └── 4f93f918ba6f_.py
├── docker-compose.yml
├── models
    ├── __init__.py
    ├── schedule.py
    └── timestamp.py
├── requirements.txt
├── resources
    ├── hello_world.py
    └── schedule.py
├── schemas
    └── schedule_schema.py
├── settings
    └── env.py
├── static
    ├── images
    │   ├── Logo_TimeSaver.png
    │   ├── ampulheta.webp
    │   └── favicon.ico
    ├── js
    │   └── index.js
    └── style.css
└── templates
    ├── create.html
    ├── index.html
    ├── layout.html
    └── update.html
```
