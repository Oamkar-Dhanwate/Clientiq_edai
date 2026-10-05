# ClientIQ Prerequisites

This file is the single setup checklist to complete before running, coding, seeding data, indexing vectors, or demoing ClientIQ.

## Local Machine

| Requirement | Version / Value | Why It Is Needed |
|-------------|-----------------|------------------|
| Python | 3.10+ | Backend, agents, ML, data generation. Verified locally with Python 3.10.11. |
| pip | Bundled with Python | Dependency installation. |
| Git | Latest stable | Version control and project submission. |
| Docker Desktop | Latest stable | TiDB and full Docker Compose deployment. |
| MySQL client | 8.x compatible | Applying schema and debugging TiDB. |
| Modern browser | Chrome/Edge/Firefox | Frontend and API docs. |
| Optional GPU | Any CUDA-capable GPU | Faster local embedding/model work, not required. |

## Accounts and Keys

| Service | Required | Environment Variable |
|---------|----------|----------------------|
| Groq | Yes for LLM responses | `GROQ_API_KEY` |
| Pinecone | Yes for vector retrieval/indexing | `PINECONE_API_KEY` |
| TiDB Cloud | Optional if not using Docker TiDB | `TIDB_HOST`, `TIDB_USER`, `TIDB_PASSWORD` |

## Environment Variables

Create `.env` in the project root with these values.

```env
APP_NAME=ClientIQ
APP_ENV=development
APP_SECRET_KEY=change-me-locally
APP_DEBUG=true

TIDB_HOST=localhost
TIDB_PORT=4000
TIDB_USER=root
TIDB_PASSWORD=
TIDB_DATABASE=clientiq
TIDB_SSL=false

PINECONE_API_KEY=
PINECONE_ENVIRONMENT=us-east-1-aws
PINECONE_INDEX_NAME=clientiq-docs

LLM_PROVIDER=groq
GROQ_API_KEY=
GROQ_BASE_URL=https://api.groq.com/openai/v1
GROQ_MODEL=llama-3.1-8b-instant

# Optional fallback provider config
MISTRAL_API_KEY=
MISTRAL_BASE_URL=https://api.mistral.ai/v1
MISTRAL_MODEL=mistral-small-latest

EMBEDDING_MODEL=BAAI/bge-small-en-v1.5
EMBEDDING_DIMENSION=384

JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=480

CHUNK_SIZE=512
CHUNK_OVERLAP=64
TOP_K_RESULTS=5

LOG_LEVEL=INFO
LOG_FILE=logs/clientiq.log
```

## Python Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

For exact reproduction of the verified local environment, install from `requirements.lock` instead.

On macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For exact reproduction of the verified local environment, install from `requirements.lock` instead.

## Database Setup

Use one of these options.

| Option | Use When | Command |
|--------|----------|---------|
| Docker TiDB | Local development and demo | `docker compose up tidb tidb-init` |
| TiDB Cloud | Cloud demo/research deployment | Configure TiDB variables in `.env`, then apply `backend/database/schema.sql`. |

Manual schema command:

```bash
mysql -h %TIDB_HOST% -P %TIDB_PORT% -u %TIDB_USER% -p%TIDB_PASSWORD% < backend/database/schema.sql
```

## Data and Vector Index Setup

Run these only after the database and `.env` are ready.

```bash
python -m data_generation.seed_all
python -m data_generation.embed_and_index
```

Expected output:

- synthetic companies, contacts, opportunities, communications, tickets, contracts, calls, meetings
- TiDB rows for CRM and analytics
- Pinecone vectors with source metadata

## Run the App

```bash
uvicorn backend.api.main:app --reload --port 8000
```

Open:

- frontend: `http://localhost:8000`
- API docs: `http://localhost:8000/api/docs`
- health: `http://localhost:8000/api/health`

## Demo Credentials

| Role | Email | Password |
|------|-------|----------|
| Admin | `admin@clientiq.demo` | `admin123` |
| Manager | `manager@clientiq.demo` | `manager123` |
| Analyst | `analyst@clientiq.demo` | `analyst123` |
| Viewer | `viewer@clientiq.demo` | `viewer123` |

## Pre-Code Execution Gate

Before adding a feature, confirm these documents exist and are updated:

- `docs/SRS.md`
- `docs/PROMPT_PIPELINE.md`
- `docs/SKILLS_AND_AGENTS.md`
- `docs/VERSION_SYNC.md`
- `docs/architecture.md`
- `docs/api_reference.md`
- `ClientIQ_2.0_TODO.md`

## Common Failure Checks

| Symptom | Check |
|---------|-------|
| API starts in degraded mode | TiDB or Groq health check failed. |
| RAG returns no context | Pinecone key/index missing or `embed_and_index` not run. |
| Login fails | Seed data or auth table not initialized. |
| SQL agent errors | TiDB schema not applied or database env mismatch. |
| Slow first query | Local embedding/model import is warming up. |
