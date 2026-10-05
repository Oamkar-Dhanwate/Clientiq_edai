# ClientIQ Project Continuation Guide

Use this file as the control room for continuing ClientIQ without losing synchronization between code, TODOs, prompts, docs, and versions.

## Current State

ClientIQ currently has a working 1.0.0 baseline with:

- FastAPI backend.
- Vanilla frontend.
- TiDB schema.
- Pinecone RAG modules.
- Groq-backed OpenAI-compatible LLM client.
- 11 LangGraph agents.
- Synthetic data generation scripts.
- Docker Compose support.
- Verified local Python environment based on Python 3.10.11 and `requirements.lock`.

`ClientIQ_2.0_TODO.md` defines the target 2.0 major-project roadmap. Treat it as the roadmap, not proof that every feature already exists.

## Documentation Map

| Need | File |
|------|------|
| What the system must do | `docs/SRS.md` |
| What must be installed/configured | `docs/PREREQUISITES.md` |
| How versions stay synchronized | `docs/VERSION_SYNC.md` |
| How prompts and agent pipelines work | `docs/PROMPT_PIPELINE.md` |
| Which engineering skills and agents exist | `docs/SKILLS_AND_AGENTS.md` |
| Governance, security, approvals, recovery | `docs/GOVERNANCE_AND_OPERATIONS.md` |
| RAG, ML, KPI, and business success metrics | `docs/EVALUATION_AND_SUCCESS_METRICS.md` |
| How the system is architected | `docs/architecture.md` |
| API behavior | `docs/api_reference.md` |
| Work backlog | `ClientIQ_2.0_TODO.md` |

## Pre-Code Execution Checklist

Before implementing a new feature:

- Identify the matching item in `ClientIQ_2.0_TODO.md`.
- Confirm whether it is P0, P1, P2, or P3.
- Update `docs/SRS.md` if the requirement changes.
- Update `docs/PROMPT_PIPELINE.md` if agent behavior or prompts change.
- Update `docs/SKILLS_AND_AGENTS.md` if adding or changing an agent.
- Update `docs/PREREQUISITES.md` if setup, keys, services, or commands change.
- Update `docs/VERSION_SYNC.md` if a package, API version, model, or product version changes.
- Update `docs/GOVERNANCE_AND_OPERATIONS.md` if the feature touches roles, data, approvals, observability, audit, or recovery.
- Update `docs/EVALUATION_AND_SUCCESS_METRICS.md` if the feature changes KPIs, RAG behavior, ML behavior, or demo success claims.

## Roadmap Crosswalk

| Priority | TODO Items | Current Repo Match | Next Best Work |
|----------|------------|--------------------|----------------|
| P0 | Customer 360 | frontend clients page, clients API, schema | verify full profile completeness and tests |
| P0 | Hybrid RAG | `backend/rag/`, retrieval agent, Pinecone settings | add source tracking, stale-vector handling, eval set |
| P0 | LangGraph multi-agent system | `backend/graph/`, 11 agents | add routing tests and failure recovery |
| P0 | CRM SQL Agent | `backend/agents/crm_sql_agent.py` | harden read-only SQL validation |
| P0 | Knowledge Graph | graph route, graph service, KG agent | document node/edge schema and add graph tests |
| P0 | Churn Prediction | risk agent, ML modules | add explainability and model metrics |
| P0 | Explainable AI | planned | add SHAP or feature-driver explanation |
| P0 | Recommendation Engine | recommendation agent | connect actions to measurable outcomes |
| P0 | Analytics Dashboard | dashboard and analytics route | add forecast/risk drill-downs |
| P1 | Sales Forecasting | planned | define data contract first |
| P1 | Meeting Intelligence | planned | define transcript schema first |
| P1 | AI Email Assistant | planned | define approval and prompt templates first |
| P1 | RAG Evaluation | planned | create evaluation dataset and metrics |
| P1 | Enterprise Security | partial | RBAC, PII masking, injection tests |
| P1 | Customer Health Score | health snapshots exist | formalize scoring formula |
| P1 | Business KPI Definitions | partial | use `docs/EVALUATION_AND_SUCCESS_METRICS.md` as KPI contract |
| P1 | Data Governance | planned | implement metadata, retention, deletion, classification rules |
| P1 | ML/Model Governance | planned | add model registry and release gate |
| P1 | Auditability | foundation exists | add event coverage and correlation IDs |
| P1 | Production Observability | basic request timing | add metrics, alert thresholds, token/cost tracking |
| P1 | Human Approval Workflows | planned | add approval states before outbound actions |
| P2 | Voice Assistant | planned | select STT/TTS provider |
| P2 | Real-Time Pipeline | planned | event schema before Kafka |
| P2 | MLOps/Monitoring | planned | add model/data version tables |
| P2 | Disaster Recovery | missing | run restore drill and document RPO/RTO |
| P3 | Research and polish | planned | build reproducible results package |

## Suggested Implementation Order

1. Stabilize documentation, `.env.example`, setup, and version sync.
2. Keep the local `.venv` synchronized with `requirements.txt` and `requirements.lock`.
3. Add tests for current routes, agents, and routing.
4. Harden security: RBAC, SQL validation, prompt-injection checks.
5. Improve retrieval: metadata schema, document IDs, stale-vector sync.
6. Add RAG/LLM evaluation.
7. Add churn explainability.
8. Formalize governance: audit events, approval states, model registry, and recovery drill.
9. Add forecasting or meeting intelligence as the first P1 differentiator.
10. Prepare academic report, PPT, demo script, and evaluation tables.

## Done Means

A TODO item is complete only when:

- code is implemented
- prompt changes are documented
- setup changes are documented
- API/architecture docs are updated
- tests or manual verification steps are recorded
- demo impact is clear
- version impact is checked
- governance impact is checked
- evaluation or business metric impact is checked

## Guardrails

- Do not overwrite existing files for convenience.
- Prefer additive docs and small targeted patches.
- Keep implementation aligned with existing OOP agent/service patterns.
- Do not introduce new frameworks unless they remove real complexity.
- Keep secrets out of the repository.
- Keep prompts short enough to evaluate and version.
