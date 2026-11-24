# Arquitetura — Exportacate

## 1. Visão geral

O sistema segue uma arquitetura **cliente-servidor desacoplada**:

- **Frontend**: aplicação React/Next.js, responsável pela interface e consumo
  da API via requisições HTTP (fetch/axios).
- **Backend**: API REST em Flask, organizada em 3 camadas, responsável pelas
  regras de negócio e persistência dos dados.
- **Banco de dados**: relacional (PostgreSQL ou MySQL), acessado via ORM
  (SQLAlchemy).

```
[ Next.js + React + Tailwind ]  <-- HTTP/JSON -->  [ Flask API ]  <-->  [ PostgreSQL/MySQL ]
        (Vercel)                                   (rotas / serviços / modelos)
```

## 2. Repositório de código

- Código-fonte versionado em repositório **público no GitHub**.
- Estrutura sugerida:

```
exportacate/
├── backend/
│   ├── app/
│   │   ├── models/      # camada de modelos (SQLAlchemy)
│   │   ├── services/    # camada de serviços (regras de negócio)
│   │   ├── routes/      # camada de rotas (endpoints Flask)
│   │   ├── __init__.py
│   │   └── config.py
│   ├── requirements.txt
│   └── run.py
├── frontend/
│   ├── app/              # páginas Next.js (App Router)
│   ├── components/
│   ├── package.json
│   └── tailwind.config.js
├── docs/
│   ├── miniworld.md
│   ├── architecture.md
│   └── screenshots/      # prints de execução local
└── README.md
```

- O `README.md` na raiz deve conter: descrição do projeto, pré-requisitos,
  passo a passo para instalar e rodar backend e frontend localmente, link do
  sistema hospedado e prints de execução.

## 3. Backend

- **Linguagem/Framework**: Python + Flask
- **ORM**: SQLAlchemy
- **Banco de dados**: PostgreSQL ou MySQL
- **Organização em 3 camadas**:
  1. **Modelos** (`app/models`): classes SQLAlchemy que representam as
     entidades do minimundo (Fazenda, Pomar, LoteColheita, InspecaoQualidade,
     Embalagem, Embarque, ClienteImportador, Pedido, DocumentoExportacao,
     Pagamento, Funcionario) e seus relacionamentos.
  2. **Serviços** (`app/services`): regras de negócio (ex.: validar se um
     lote pode ser aprovado, calcular peso total de um embarque, atualizar
     status de pagamento). Os serviços não conhecem detalhes de HTTP.
  3. **Rotas** (`app/routes`): endpoints REST (Blueprints do Flask) que
     recebem a requisição, chamam os serviços e devolvem JSON.
- Exemplo de fluxo: `POST /lotes` → rota valida payload → chama
  `LoteService.criar_lote()` → serviço usa `LoteColheita` (modelo) para
  persistir no banco → rota retorna JSON de resposta.
- Autenticação (se aplicável): JWT simples entre frontend e backend.
- CORS habilitado para permitir chamadas do domínio do frontend (Vercel).

## 4. Frontend

- **Framework**: Next.js (React)
- **Estilização**: Tailwind CSS
- Páginas principais: Dashboard, Fazendas/Pomares, Lotes de Colheita,
  Inspeções, Embalagens/Embarques, Clientes, Pedidos, Pagamentos.
- Consome a API do backend via variável de ambiente
  `NEXT_PUBLIC_API_URL`, apontando para a URL do backend hospedado.

## 5. Hospedagem

- **Frontend**: hospedado na **Vercel**, a partir do repositório GitHub
  (deploy automático a cada push na branch principal).
- **Backend + banco de dados**: hospedados em um serviço compatível com
  aplicações Flask persistentes (ex.: Render, Railway ou similar), já que a
  Vercel é otimizada para frontend/serverless. A URL pública da API é
  configurada no frontend via variável de ambiente.
- **Variáveis de ambiente** (exemplo):
  - Backend: `DATABASE_URL`, `SECRET_KEY`
  - Frontend: `NEXT_PUBLIC_API_URL`

## 6. Dados de exemplo

O banco é populado com um script de *seed* (`backend/app/seed.py`) contendo
dados coerentes: fazendas e pomares fictícios, lotes de colheita, inspeções,
embarques, clientes importadores (ex.: EUA, Países Baixos, Espanha), pedidos
e pagamentos, para permitir a demonstração completa do fluxo do sistema.
