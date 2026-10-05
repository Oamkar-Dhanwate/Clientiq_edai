# ClientIQ Version Synchronization

## Current Version Contract

| Area | Current Value | Source | Notes |
|------|---------------|--------|-------|
| Product roadmap | ClientIQ 2.0 | `ClientIQ_2.0_TODO.md` | Target academic/project scope. |
| Implemented application | 1.0.0 | `README.md`, `backend/api/main.py`, frontend footer | Existing working baseline. |
| API version | 1.0.0 | `backend/api/main.py` | FastAPI metadata and health response. |
| Python runtime | 3.10+ | `README.md`, `docs/PREREQUISITES.md`, `setup.py` | Verified locally with Python 3.10.11. |
| Agent count implemented | 11 | `backend/graph/workflow.py` | Supervisor, Compliance, CRM SQL, Retrieval, Memory, Sentiment, Analytics, Risk, Recommendation, Knowledge Graph, Citation. |
| LLM provider | Groq | `backend/utils/config.py`, `backend/services/mistral_client.py` | Default model: `llama-3.1-8b-instant`, OpenAI-compatible base URL `https://api.groq.com/openai/v1`. |
| Embedding model | BAAI/bge-small-en-v1.5 | `backend/utils/config.py`, `backend/rag/embedder.py` | 384-dimensional embeddings. |
| Backend framework | FastAPI 0.111.0 | `requirements.txt` | Served by Uvicorn. |
| Agent framework | LangGraph 0.1.1 | `requirements.txt` | Stateful graph orchestration. |
| Database | TiDB/MySQL-compatible | `backend/database/schema.sql`, `docker-compose.yml` | Default port `4000`. |
| Vector database | Pinecone | `requirements.txt`, `backend/rag/` | Index: `clientiq-docs` by default. |

## Synchronization Rule

ClientIQ should be treated as:

- **ClientIQ 1.0.0**: implemented baseline currently in the repository.
- **ClientIQ 2.0**: planned major project expansion described in `ClientIQ_2.0_TODO.md`.

Do not relabel the application as fully 2.0 until the P0 items in `ClientIQ_2.0_TODO.md` are implemented, tested, and documented.

## Recommended Release Path

| Release | Meaning | Required Evidence |
|---------|---------|-------------------|
| 1.0.0 | Current multi-agent CRM intelligence baseline | Existing FastAPI app, 11-agent graph, CRM/RAG/analytics UI. |
| 1.1.0 | Documentation and reproducibility hardening | SRS, prerequisites, prompt pipeline, `.env.example`, setup validation. |
| 1.2.0 | Data and retrieval reliability | data quality checks, document IDs, source tracking, stale-vector detection. |
| 1.5.0 | Evaluation-ready AI system | RAG evaluation, prompt injection tests, citation tests, latency/cost metrics. |
| 2.0.0 | Final major project system | P0 complete plus selected P1 differentiators and final academic documentation. |

## Code Synchronization Checklist

Before changing the version number, update these together:

- `README.md` badge and setup text.
- `backend/api/main.py` FastAPI `version`.
- `backend/api/main.py` `/api/health` response version.
- `frontend/index.html` footer/version label.
- `setup.py` package metadata.
- `requirements.txt` and `requirements.lock` when dependency behavior changes.
- This file.
- Any presentation/report screenshots that display version text.

## Dependency Pinning Rule

Keep package versions pinned in `requirements.txt` during the final-year project phase. Upgrade only when a task needs it, then record:

- package name
- old version
- new version
- reason
- test command/output
- rollback note

Use `requirements.txt` for curated direct dependencies. Use `requirements.lock` for exact reproduction of the verified local environment, including transitive dependencies.

## Documentation Synchronization Rule

For every completed TODO item, update the matching documentation:

| TODO Area | Documentation File |
|-----------|--------------------|
| Requirements, scope, users | `docs/SRS.md` |
| Setup and prerequisites | `docs/PREREQUISITES.md` |
| Prompting and agent behavior | `docs/PROMPT_PIPELINE.md` |
| Agent roles and skills | `docs/SKILLS_AND_AGENTS.md` |
| Architecture changes | `docs/architecture.md` |
| API changes | `docs/api_reference.md` |
| Version changes | `docs/VERSION_SYNC.md` |
| Security, governance, approvals, recovery | `docs/GOVERNANCE_AND_OPERATIONS.md` |
| KPI, RAG, ML, business success metrics | `docs/EVALUATION_AND_SUCCESS_METRICS.md` |
