# 🥑 Exportacate

Sistema de gestão para exportação de abacates: controla o processo completo
desde a colheita na fazenda até o pagamento do pedido pelo cliente
importador no exterior.

Trabalho da disciplina de Desenvolvimento Web (AV6) — IFC.

## Documentação

- [Minimundo e entidades](docs/miniworld.md)
- [Arquitetura](docs/architecture.md)

## Equipe

| Nome | Atuação no trabalho |
|------|----------------------|
| _Gustavo_ | _Mestre Programador com IA_ |
| _João Guilherme_ | _Acessor Criativo e Apoio_ |
| _Diogo_ | _Tester e Sugestões_ |

## Stack

- **Backend**: Python 3.11+, Flask, SQLAlchemy, PostgreSQL (produção) / SQLite (desenvolvimento), gerenciado com Poetry
- **Frontend**: React, Next.js 14, Tailwind CSS
- **Hospedagem**: Vercel (frontend) + Render/Railway/similar (backend)

## Configuração de Ambiente

### Variáveis de Ambiente Principais (Backend)

| Variável | Obrigatória | Descrição |
|----------|-------------|-----------|
| `FLASK_ENV` | Não | `development`, `production` ou `testing` (padrão: `development`) |
| `SECRET_KEY` | **Sim (produção)** | Chave secreta para sessões/JWT. Gere com: `python -c "import secrets; print(secrets.token_hex(32))"` |
| `DATABASE_URL` | Não | URL do banco. Desenvolvimento: SQLite (padrão). Produção: PostgreSQL (`postgresql://user:pass@host:5432/db`) |
| `FRONTEND_URL` | Não | Origem(es) permitida(s) para CORS. Desenvolvimento: `http://localhost:3000` (padrão). Produção: domínio do frontend |
| `SQLALCHEMY_ECHO` | Não | Log de queries SQL (`true`/`false`, padrão: `false`) |
| `PORT` | Não | Porta do servidor (padrão: 5000) |

### Variáveis de Ambiente (Frontend)

| Variável | Obrigatória | Descrição |
|----------|-------------|-----------|
| `NEXT_PUBLIC_API_URL` | Sim | URL da API backend (ex.: `http://localhost:5000`) |

## Como rodar localmente

### Pré-requisitos

- Python 3.11+
- Node.js 18+
- Poetry (gerenciador de dependências do backend)
- PostgreSQL opcional (desenvolvimento usa SQLite por padrão)

### Backend

```bash
cd backend

# instalar dependências com Poetry (cria venv automaticamente)
poetry install

# configurar variáveis de ambiente (ver backend/.env.example)
cp .env.example .env
# edite .env conforme necessário

# ativar o ambiente virtual do Poetry
poetry shell

# criar/popular o banco (usa SQLite local por padrão)
flask db upgrade
# python app/seed.py  # será implementado futuramente

# iniciar o servidor
python run.py
# ou: poetry run python run.py
```

> **Nota:** O Poetry gerencia o ambiente virtual automaticamente. Use `poetry shell` para ativá-lo ou prefixe comandos com `poetry run` (ex.: `poetry run flask db upgrade`).

A API sobe por padrão em `http://localhost:5000`.

### Frontend

```bash
cd frontend
npm install

# configurar variável de ambiente apontando para o backend local
echo "NEXT_PUBLIC_API_URL=http://localhost:5000" > .env.local

npm run dev
```

O frontend sobe em `http://localhost:3000`.

### Executar Testes (Backend)

```bash
cd backend
poetry run pytest
# ou com cobertura:
poetry run pytest --cov=app --cov-report=term-missing
```

## Deploy

### Backend (Produção)
- Configure `FLASK_ENV=production`
- Defina `SECRET_KEY` forte no ambiente
- Configure `DATABASE_URL` para PostgreSQL (ex.: Render, Railway, Neon, Supabase)
- Configure `FRONTEND_URL` para o domínio do frontend Vercel
- O `poetry.lock` deve ser versionado para builds reprodutíveis

### Frontend (Produção)
- Deploy automático via Vercel a partir da branch `main`
- Configure `NEXT_PUBLIC_API_URL` nas variáveis de ambiente do Vercel apontando para a URL do backend

## Links do projeto

- **Repositório**: https://github.com/Kovatsug/Exportacate
- **Sistema hospedado**: _preencher URL_

## Prints de execução local

As capturas de tela do sistema rodando localmente estão em
[`docs/screenshots`](docs/screenshots).
