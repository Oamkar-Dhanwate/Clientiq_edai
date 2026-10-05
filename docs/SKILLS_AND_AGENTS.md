# ClientIQ Skills and Agent Guide

## Engineering Skills Required

| Skill | Needed For | Repo Area |
|-------|------------|-----------|
| Python OOP | agents, services, database logic | `backend/` |
| FastAPI | REST APIs, auth, docs, middleware | `backend/api/` |
| SQL and TiDB/MySQL | CRM queries, schema, optimization | `backend/database/` |
| LangGraph | multi-agent orchestration | `backend/graph/` |
| RAG engineering | chunking, embeddings, retrieval, fusion | `backend/rag/` |
| Prompt engineering | agent prompts, routing, synthesis | `docs/PROMPT_PIPELINE.md`, `backend/agents/` |
| ML basics | churn, sentiment, forecasting | `backend/ml/`, `backend/services/` |
| Frontend JS | dashboards, charts, graph visualization | `frontend/` |
| Security | JWT, RBAC, PII, prompt injection | `backend/services/auth_service.py`, agents |
| Evaluation | RAGAS, latency, faithfulness, cost | planned `evaluation/` |

## OOP and Code Quality Rules

- Keep each agent as a class with a clear `run` or `arun` boundary.
- Keep external system access inside services or repository-style helpers.
- Keep shared state fields explicit in `backend/graph/state.py`.
- Keep route handlers thin; business logic belongs in services/agents.
- Do not duplicate prompt text across files without recording it in `docs/PROMPT_PIPELINE.md`.
- Add new configuration through `backend/utils/config.py` and `.env` variables.
- Prefer typed dictionaries/models for structured data.
- Keep SQL validation and permission checks close to the SQL agent and compliance agent.
- Optimize only after measuring latency or repeated code paths.

## Implemented Agent Inventory

| Agent | File | Responsibility |
|-------|------|----------------|
| Supervisor | `backend/agents/supervisor.py` | intent planning and final answer synthesis |
| Compliance | `backend/agents/compliance_agent.py` | RBAC, policy checks, sensitive-data control |
| CRM SQL | `backend/agents/crm_sql_agent.py` | natural-language to SQL and TiDB execution |
| Retrieval | `backend/agents/retrieval_agent.py` | semantic/vector retrieval and context collection |
| Memory | `backend/agents/memory_agent.py` | conversation and entity context |
| Sentiment | `backend/agents/sentiment_agent.py` | customer sentiment analysis |
| Analytics | `backend/agents/analytics_agent.py` | KPI and business metric computation |
| Risk | `backend/agents/risk_agent.py` | churn and renewal risk assessment |
| Recommendation | `backend/agents/recommendation_agent.py` | next-best-action generation |
| Knowledge Graph | `backend/agents/knowledge_graph_agent.py` | entity/relationship extraction and graph data |
| Citation | `backend/agents/citation_agent.py` | source attribution and confidence scoring |

## Planned 2.0 Agents

| Agent | Priority | Required Before Coding |
|-------|----------|------------------------|
| Forecasting Agent | P1 | sales forecast data contract and model metric definition |
| Email Generation Agent | P1 | approval workflow, tone/length controls, email prompt templates |
| Meeting Intelligence Agent | P1 | transcript schema, STT provider decision, action-item extraction prompt |
| Voice Agent | P2 | speech-to-text/text-to-speech provider, latency budget |

## Agent Development Checklist

Before adding or changing an agent:

- Update `docs/PROMPT_PIPELINE.md`.
- Add fields to `backend/graph/state.py` if new state is required.
- Add or update intent mapping in `backend/graph/router.py`.
- Register the node and edge in `backend/graph/workflow.py`.
- Add route/API changes if user-facing.
- Add unit tests for routing and agent output shape.
- Add prompt-injection and insufficient-evidence cases for AI-facing agents.

## Required Agent Output Shape

Every agent should update:

- `current_agent`
- `agent_trace`
- its own state fields
- `errors` when it fails recoverably

Every agent should avoid:

- writing unrelated state fields
- calling the LLM when deterministic logic is enough
- returning final user prose unless it is the final synthesis step

## Optimization Rules

- Cache stable settings with `get_settings()`.
- Reuse model clients where practical.
- Keep retrieval `top_k` configurable.
- Use async for network/database calls when it affects route latency.
- Log timings for slow agents.
- Keep expensive ML/model loading out of per-request hot paths.
