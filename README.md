# 🥑 Exportacate

Sistema de gestão para exportação de abacates: controla o processo completo
desde a colheita na fazenda até o pagamento do pedido pelo cliente
importador no exterior.

Trabalho da disciplina de Desenvolvimento Web (AV6) — IFC.

## Documentação

- [Minimundo e entidades](miniworld.md)
- [Arquitetura](architecture.md)

## Stack

- **Backend**: Python, Flask, SQLAlchemy, PostgreSQL/MySQL
- **Frontend**: React, Next.js, Tailwind CSS
- **Hospedagem**: Vercel (frontend) + serviço de hospedagem do backend

## Como rodar localmente

### Pré-requisitos

- Python 3.11+
- Node.js 18+
- PostgreSQL ou MySQL instalado (ou rodando via Docker)

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# configurar variáveis de ambiente (ver .env.example)
cp .env.example .env

# criar/popular o banco
flask db upgrade
python app/seed.py

# iniciar o servidor
python run.py
```

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



## Prints de execução local

As capturas de tela do sistema rodando localmente estão em
[`docs/screenshots`](docs/screenshots).
