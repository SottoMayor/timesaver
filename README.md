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

1. No `.env`, atualize a variável:

```
SQLALCHEMY_DATABASE_URI=mysql://user:password@localhost:3306/test_db
```

2. No `docker-compose.yml`, comente todo o serviço `flask_timesaver_app`.
   
---

## Entidade `Schedule`

| Campo           | Tipo     | Restrições   |
|----------------|----------|--------------|
| `id`           | int      | Primary Key  |
| `schedule_date`| date     | Not Null     |
| `schedule_time`| string     | Not Null     |
| `client`       | string   | Not Null     |
| `service`      | string   | Not Null     |

> **Obs:** Como o objetivo principal é implementar o CRUD de Agendamentos, algumas decisões foram tomadas para simplificar:

1. **Não houve normalização** das entidades `client` e `service`; foram representadas apenas como strings simples.
2. **Não há autenticação** ou controle de acesso implementado.
3. **A UI não trata erros de forma sofisticada**. Embora o Marshmallow seja usado para validar os dados, os erros são apenas exibidos diretamente na tela — o foco está na lógica e na persistência dos dados.

---

## Endpoints disponíveis

### [GET] `/schedules`
Lista todos os agendamentos, com suporte a filtros opcionais via query string:

```
/schedules?date={date}&client={client}&service={service}
```

### [GET] `/schedules/create`
Renderiza o formulário para criar um novo agendamento.

### [POST] `/schedules`
Cria um novo agendamento com base nos dados do formulário.

**Body esperado:**

```
{
  schedule_date: string,
  schedule_time: string,
  client: string,
  service: string
}
```

### [GET] `/schedules/update/<id>`
Carrega o formulário preenchido para editar um agendamento existente.

### [POST] `/schedules/update/<id>`
Atualiza os dados de um agendamento.

**Body esperado:**

```
{
  schedule_date: string,
  schedule_time: string,
  client: string,
  service: string
}
```

### [POST] `/schedules/delete/<id>`
Remove o agendamento com o ID informado.

## Observações sobre o uso de Jinja (Template Engine)

> Como este projeto utiliza Jinja para renderizar os templates HTML:

1. Só existem métodos `GET` e `POST` nas rotas — não há uso de `PATCH` ou `DELETE` diretamente no navegador.
2. Todos os dados enviados pelo `body` (formulários) chegam como **string**.
3. 
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
- SGBD: `MySQL`

**Docker:**

- `docker-compose.yml` sobe o banco de dados.
- Volume configurado para **persistência de dados**.

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
  - Sobe o app + banco de dados juntos.
  - Banco com volume de dados persistente.

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
    │       └── ca35d5158a91_.py
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
    └── style.css
└── templates
    ├── create.html
    ├── index.html
    ├── layout.html
    └── update.html
```
