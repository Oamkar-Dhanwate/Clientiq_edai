# ClientIQ 2.0 Software Requirements Specification

## 1. Purpose

ClientIQ 2.0 is an enterprise customer intelligence platform for sales, customer success, and management teams. It combines CRM data, communication records, support history, contracts, knowledge graphs, hybrid retrieval, predictive analytics, and multi-agent AI to answer business questions and recommend next actions.

This SRS aligns the implemented repository with the roadmap in `ClientIQ_2.0_TODO.md`.

## 2. Scope

ClientIQ 2.0 will provide:

- Customer 360 profiles.
- Natural-language CRM and document intelligence.
- Hybrid RAG over structured TiDB data and Pinecone vectors.
- LangGraph-based multi-agent orchestration.
- Customer churn risk prediction and explanations.
- Sentiment and customer health intelligence.
- Knowledge graph visualization and reasoning.
- Next-best-action recommendations.
- Admin, audit, and RBAC controls.
- Evaluation artifacts for final-year academic submission.

## 3. Current Baseline

The repository currently includes:

- FastAPI backend with auth, query, analytics, clients, graph, and admin routes.
- Vanilla HTML/CSS/JS frontend pages.
- TiDB schema and SQLAlchemy models.
- Pinecone-based RAG components.
- 11 LangGraph agents.
- Groq-backed OpenAI-compatible LLM client.
- Churn, sentiment, analytics, and graph services.
- Synthetic data generation scripts.
- Docker Compose configuration for TiDB and API deployment.

## 4. Users and Roles

| Role | Primary Needs | Access Level |
|------|---------------|--------------|
| Admin | users, audit logs, system monitoring, configuration | full system |
| Manager | revenue, churn, forecasts, portfolio analytics | CRM plus financial analytics |
| Sales / Customer Success | customer profile, interactions, recommendations | customer-facing intelligence |
| Analyst | trends, KPIs, RAG evaluation, reporting | analytics and read access |
| Viewer | customer and dashboard visibility | read-only |

## 5. Functional Requirements

| ID | Requirement | Priority | Current Status |
|----|-------------|----------|----------------|
| FR-001 | User login with JWT authentication | P0 | Implemented baseline |
| FR-002 | Role-based access checks | P0 | Partial baseline |
| FR-003 | Customer list and Customer 360 profile | P0 | Implemented baseline |
| FR-004 | Natural-language query endpoint | P0 | Implemented baseline |
| FR-005 | Supervisor routes query to specialized agents | P0 | Implemented baseline |
| FR-006 | CRM SQL agent converts business questions to SQL | P0 | Implemented baseline |
| FR-007 | Retrieval agent searches vector context | P0 | Implemented baseline |
| FR-008 | Citation agent attaches evidence and confidence | P0 | Implemented baseline |
| FR-009 | Analytics agent computes KPIs | P0 | Implemented baseline |
| FR-010 | Risk agent predicts churn risk | P0 | Implemented baseline |
| FR-011 | Recommendation agent suggests next actions | P0 | Implemented baseline |
| FR-012 | Knowledge graph API and visualization | P0 | Implemented baseline |
| FR-013 | Document upload and ingestion pipeline | P1 | Planned |
| FR-014 | RAG evaluation dashboard | P1 | Planned |
| FR-015 | Explainable AI with SHAP | P1 | Planned |
| FR-016 | Sales forecasting | P1 | Planned |
| FR-017 | Meeting transcription and intelligence | P1 | Planned |
| FR-018 | AI email assistant | P1 | Planned |
| FR-019 | Voice assistant | P2 | Planned |
| FR-020 | Real-time event pipeline | P2 | Planned |
| FR-021 | Human approval workflow for outbound/high-impact actions | P1 | Planned |
| FR-022 | RAG evaluation dataset and metrics dashboard | P1 | Planned |
| FR-023 | Business KPI definitions and Customer Health formula | P1 | Documented |
| FR-024 | Disaster recovery restore procedure | P2 | Documented |

## 6. Non-Functional Requirements

| ID | Requirement | Target |
|----|-------------|--------|
| NFR-001 | API response time | p95 under 3 seconds for non-LLM endpoints. |
| NFR-002 | AI response time | p95 under 15 seconds for standard RAG queries. |
| NFR-003 | Availability | Local demo should recover gracefully if LLM/vector services are unavailable. |
| NFR-004 | Security | JWT, RBAC, input validation, PII masking, audit logging. |
| NFR-005 | Maintainability | OOP service/agent boundaries, typed state, pinned dependencies. |
| NFR-006 | Observability | request timing, logs, agent trace, cost/token tracking for future work. |
| NFR-007 | Reproducibility | seed scripts, schema, setup docs, deterministic evaluation datasets. |
| NFR-008 | Explainability | citations for RAG answers and human-readable ML explanations. |
| NFR-009 | Governance | data classification, retention, deletion, audit, and approval rules documented and enforced. |
| NFR-010 | Recovery | database, vector index, source data, model artifacts, and logs have restore procedures. |
| NFR-011 | Evaluation | RAG, ML, KPI, and business success metrics are versioned and reproducible. |

## 7. Data Requirements

ClientIQ must manage:

- companies
- contacts
- opportunities
- emails
- meetings
- call transcripts
- support tickets
- contracts
- health snapshots
- sentiment timeline
- knowledge graph entities and relationships
- users, roles, audit logs, agent sessions

Planned 2.0 additions:

- invoices/payment information
- product/service usage
- document ingestion status
- model registry metadata
- evaluation datasets and results
- approval workflow records
- data classification and retention metadata

## 8. AI Requirements

| Component | Requirement |
|-----------|-------------|
| Prompt pipeline | Stored and reviewed in `docs/PROMPT_PIPELINE.md`. |
| Routing | Intent classification must select the minimum required agent set. |
| Grounding | Final answers must prefer SQL/RAG/graph evidence over model prior knowledge. |
| Citations | Important factual answers must include source references where available. |
| Safety | SQL must be read-only and user role aware. |
| Failure behavior | Missing evidence must produce an insufficient-evidence response, not fabricated facts. |
| Traceability | Each query must keep an agent execution trace. |
| Human approval | AI-generated emails, external notifications, discounts, CRM updates, and escalations require approval before execution. |
| Evaluation | RAG and ML behavior must be measured against versioned datasets before final claims. |

## 9. Governance Requirements

Governance controls are defined in `docs/GOVERNANCE_AND_OPERATIONS.md`.

| Area | Requirement |
|------|-------------|
| Security/RBAC | role matrix, route authorization, agent-level compliance, and SQL read-only validation |
| Data governance | classification, source metadata, retention, deletion, and vector synchronization |
| ML governance | model registry, dataset version, feature version, metrics, approval, and rollback |
| Auditability | login, API, AI query, SQL, upload, recommendation, approval, and admin events |
| Observability | API, agent, RAG, LLM, database, vector, and ML metrics |
| Human approval | explicit draft, review, approval, rejection, execution, and expiry states |
| Disaster recovery | documented RPO/RTO, backups, and restore drill |

## 10. Acceptance Criteria

The 2.0 project is accepted when:

- P0 roadmap items are implemented.
- The app runs from documented setup steps.
- Natural-language questions can combine CRM, RAG, analytics, risk, and recommendation evidence.
- Security and RBAC are demonstrated.
- RAG/LLM evaluation results are reproducible.
- Churn predictions include explanations.
- Business KPIs have documented definitions and formulas.
- Human approval is enforced for outbound/high-impact AI actions.
- Disaster recovery has been tested at least once.
- Final report, PPT, demo video, and viva notes are complete.

## 11. Traceability to TODO

| TODO Section | SRS Coverage |
|--------------|--------------|
| 0. Project Foundation | Scope, users, versioning, architecture docs. |
| 1-3. Data and storage | Data requirements and prerequisites. |
| 4-7. RAG, agents, SQL, graph | AI requirements and prompt pipeline. |
| 8-11. Churn, health, recommendations | Functional requirements. |
| 12-15. Meeting, email, voice, real-time | P1/P2 planned features. |
| 16, 20, 21. Evaluation, MLOps, testing | Non-functional and acceptance criteria. |
| 17. Security & Enterprise Features | Governance and operations controls. |
| 24-26. Documentation and deliverables | Acceptance criteria and final deliverables. |
