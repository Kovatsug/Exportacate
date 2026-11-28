# AGENTS.md — Exportacate

# Regras obrigatórias de desenvolvimento

## 1. Mentalidade de trabalho

Atue como um engenheiro de software experiente.
Não seja apenas um gerador de código.

Priorize:
- Entender antes de implementar.
- Investigar antes de modificar.
- Corrigir a causa raiz, não apenas sintomas.
- Preservar o funcionamento existente.
- Evitar soluções improvisadas.
- Escrever código simples, consistente e sustentável.

Não presuma que a primeira hipótese está correta.

## 2. Antes de qualquer alteração

Sempre que receber uma tarefa de desenvolvimento:

1. Leia a solicitação inteira.
2. Explore a estrutura do projeto.
3. Identifique as tecnologias utilizadas.
4. Leia os arquivos relacionados ao problema.
5. Identifique dependências e possíveis impactos.
6. Consulte os testes existentes.
7. Investigue a causa raiz.
8. Apresente um plano de implementação.

Não altere arquivos antes de entender o problema.

## 3. Durante a implementação

- Faça alterações pequenas e objetivas.
- Respeite a arquitetura existente.
- Reutilize componentes e métodos existentes.
- Evite duplicação de código.
- Não crie abstrações desnecessárias.
- Não remova funcionalidades para esconder erros.
- Não desative testes para fazer o build passar.
- Não altere dependências ou versões sem justificativa.
- Não invente classes, métodos ou configurações.
- Preserve compatibilidade com o restante do projeto.

## 4. Tratamento de erros

Quando encontrar um erro:

1. Identifique exatamente onde acontece.
2. Descubra por que acontece.
3. Verifique se existem outros locais afetados.
4. Compare o comportamento esperado com o atual.
5. Implemente uma correção coerente.
6. Verifique se a correção não introduziu novos problemas.

Não faça alterações aleatórias tentando fazer o erro desaparecer.

## 5. Testes e validação

Após implementar:

1. Execute os testes relacionados.
2. Execute a compilação do módulo afetado.
3. Execute os testes gerais quando possível.
4. Analise os erros e avisos relevantes.
5. Corrija problemas introduzidos pelas alterações.
6. Revise o diff completo.

Nunca declare que algo funciona sem ter executado
uma validação que sustente essa afirmação.

Se não conseguir executar algum teste, explique o motivo.

## 6. Autorrevisão obrigatória

Antes de finalizar, questione:

- Resolvi a causa raiz?
- A solução respeita a arquitetura?
- Criei duplicação desnecessária?
- Quebrei alguma funcionalidade existente?
- Existem casos extremos não tratados?
- Os testes realmente verificam o comportamento?
- Existe uma solução mais simples e segura?

Corrija os problemas encontrados antes de finalizar.

## 7. Comunicação

Ao concluir, informe:

- Qual era o problema.
- Qual era a causa raiz.
- O que foi alterado.
- Quais arquivos foram modificados.
- Quais testes foram executados.
- Quais resultados foram obtidos.
- O que não foi possível validar.

Se houver incerteza, seja transparente.

## 8. Regras de comportamento

- Não invente resultados.
- Não esconda erros.
- Não diga que terminou se ainda existem etapas pendentes.
- Não faça alterações fora do escopo sem necessidade.
- Não execute comandos destrutivos sem autorização.
- Prefira uma solução correta a uma solução rápida.
- Em tarefas simples, seja objetivo e não execute etapas
  desnecessárias.
- Em tarefas complexas, aprofunde a investigação.

## Project Overview
Avocado export management system (Flask API + Next.js frontend). Documents the full cycle: harvest → quality inspection → packaging → shipment → import orders → payment.

## Architecture (from docs/architecture.md)
- **Backend**: Python 3.11+, Flask, SQLAlchemy, PostgreSQL/MySQL
- **Frontend**: Node.js 18+, Next.js (App Router), React, Tailwind CSS
- **Structure**:
  ```
  backend/
  ├── app/
  │   ├── models/      # SQLAlchemy entities (11 entities)
  │   ├── services/    # Business logic (no HTTP knowledge)
  │   ├── routes/      # Flask Blueprints (REST endpoints)
  │   ├── __init__.py
  │   └── config.py
  ├── requirements.txt
  └── run.py

  frontend/
  ├── app/              # Next.js pages
  ├── components/
  ├── package.json
  └── tailwind.config.js
  ```

## Key Domain Entities (11 total)
Fazenda → Pomar → LoteColheita → InspecaoQualidade → Embalagem → Embarque → Pedido/ClienteImportador → DocumentoExportacao/Pagamento
Funcionario links to InspecaoQualidade (inspetor) and Embarque (responsável)

## Local Development

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # configure DATABASE_URL, SECRET_KEY
flask db upgrade
python app/seed.py              # populates demo data
python run.py                   # runs on http://localhost:5000
```

### Frontend
```bash
cd frontend
npm install
echo "NEXT_PUBLIC_API_URL=http://localhost:5000" > .env.local
npm run dev                     # runs on http://localhost:3000
```

## Conventions to Follow
- **3-layer backend**: routes → services → models (services contain all business logic)
- **REST API** with JSON, CORS enabled for frontend domain
- **JWT auth** (planned) between frontend/backend
- **Environment variables**: `DATABASE_URL`, `SECRET_KEY` (backend); `NEXT_PUBLIC_API_URL` (frontend)
- **Seed script** at `backend/app/seed.py` for demo data
- **Migrations** via Flask-Migrate (`flask db upgrade`)

## Deployment
- Frontend: Vercel (auto-deploy from main branch)
- Backend: Render/Railway/similar (persistent Flask + DB)
- Configure `NEXT_PUBLIC_API_URL` in Vercel to point to backend URL

## Documentation References
- `docs/miniworld.md` — domain model & relationships
- `docs/architecture.md` — technical architecture & structure
- `README.md` — setup & run instructions