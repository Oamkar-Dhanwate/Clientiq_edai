# ClientIQ Governance and Operations

This document formalizes the operational controls that are needed before ClientIQ can be considered enterprise-ready. It strengthens security/RBAC, data governance, ML governance, auditability, observability, human approvals, and disaster recovery.

## 1. Security and RBAC

## Role Matrix

| Capability | Admin | Manager | Sales/CS | Analyst | Viewer |
|------------|-------|---------|----------|---------|--------|
| Login and view dashboard | yes | yes | yes | yes | yes |
| View customer profile | yes | yes | assigned/customers | yes | read-only |
| View revenue/contract values | yes | yes | assigned/customers | aggregated only | no |
| Run AI query | yes | yes | yes | yes | limited |
| Run CRM SQL agent | yes | yes | scoped | read-only aggregate | no |
| View audit logs | yes | no | no | no | no |
| Manage users/roles | yes | no | no | no | no |
| Upload documents | yes | yes | scoped | yes | no |
| Generate email/action drafts | yes | yes | yes | no | no |
| Approve outbound actions | yes | yes | assigned/customers | no | no |

## Security Controls

| Control | Requirement | Implementation Target |
|---------|-------------|-----------------------|
| JWT authentication | all protected routes require valid bearer token | `backend/services/auth_service.py` |
| Role authorization | routes and agents enforce role matrix | route dependencies plus Compliance Agent |
| Read-only SQL | SQL agent only executes validated `SELECT` statements | SQL validation before execution |
| PII masking | sensitive fields redacted by role | Compliance Agent and response serializer |
| Prompt injection defense | detect instruction override attempts | Compliance Agent before routing |
| Rate limiting | prevent abuse and runaway LLM cost | API middleware or gateway |
| Secret hygiene | no API keys in git or logs | `.env`, masked logging |
| CORS policy | no wildcard origins in production | environment-specific config |

## Security Acceptance Criteria

- Unauthorized users cannot access protected routes.
- A Viewer cannot retrieve raw financial, PII, or audit-log data.
- SQL generation rejects write/destructive statements.
- Prompt-injection test cases are logged and blocked or safely answered.
- Audit logs record user, route, intent, agent trace, and decision outcome.

## 2. Data Governance

## Data Classification

| Class | Examples | Handling |
|-------|----------|----------|
| Public | product docs, public company information | can be used in demos |
| Internal | synthetic CRM, generated meetings, analytics | available to authenticated users by role |
| Confidential | real customer revenue, contracts, support details | role-scoped and audit logged |
| Restricted | credentials, tokens, personal identifiers | never shown in prompts or responses unless explicitly allowed |

## Data Lifecycle

| Stage | Rule |
|-------|------|
| Ingestion | validate schema, source, timestamp, owner, and data class |
| Normalization | create stable customer/entity IDs |
| Storage | store structured data in TiDB and vectors in Pinecone with source metadata |
| Retrieval | apply metadata filters and RBAC before context reaches the LLM |
| Retention | define retention period per data class before production use |
| Deletion | delete SQL records and matching vectors together |
| Re-indexing | version documents and mark stale vectors before replacement |

## Required Metadata

Every ingested document or record should have:

- `source_id`
- `source_type`
- `company_id`
- `created_at`
- `updated_at`
- `ingested_at`
- `document_version`
- `data_classification`
- `owner_role`
- `retention_policy`

## 3. ML and Model Governance

## Model Registry Fields

Track each ML or LLM-dependent model/configuration with:

- model name
- model type
- version
- training dataset version
- feature version
- evaluation metrics
- approval status
- deployment date
- rollback version
- owner

## Governance Rules

- Do not replace a model without recording baseline metrics.
- Do not use a model in demo claims unless evaluation data exists.
- Churn and forecast outputs must include confidence or limitation notes.
- Prompt changes must be versioned as behavior-changing artifacts.
- Model outputs that trigger business actions require human review.

## 4. Auditability

## Audit Events

| Event | Required Fields |
|-------|-----------------|
| login | user_id, role, timestamp, status |
| API request | user_id, route, method, status, latency |
| AI query | user_id, query hash, intent, agents used, status |
| SQL execution | user_id, generated SQL hash, tables used, row count |
| document upload | user_id, source_id, file type, status |
| recommendation generated | user_id, customer_id, recommendation_id, evidence IDs |
| approval decision | approver_id, action_id, decision, reason |
| admin change | admin_id, target, before/after summary |

## Audit Rules

- Never log raw secrets or full PII.
- Store hashes or redacted snippets for sensitive prompts.
- Keep agent traces for each AI query.
- Include correlation IDs across request, agent, SQL, and LLM logs.

## 5. Production Observability

## Metrics

| Category | Metric |
|----------|--------|
| API | request count, status code, p50/p95 latency, error rate |
| Agents | agent execution time, failure count, retry count |
| RAG | retrieval latency, top-k scores, empty retrieval rate |
| LLM | token usage, cost estimate, timeout rate, model error rate |
| Database | connection status, query latency, slow query count |
| Vector DB | query latency, index size, upsert failure count |
| ML | prediction count, drift signal, confidence distribution |

## Logging Standard

Each request should carry:

- `request_id`
- `user_id`
- `session_id`
- `route`
- `intent`
- `agent_trace`
- `latency_ms`
- `status`
- `error_code`

## Alert Thresholds

| Condition | Suggested Alert |
|-----------|-----------------|
| API error rate > 5% for 10 minutes | investigate backend/service outage |
| AI p95 latency > 30 seconds | inspect LLM/vector latency |
| empty retrieval rate > 25% | inspect indexing and metadata filters |
| SQL validation failures spike | inspect prompt injection or SQL prompt regression |
| LLM timeout rate > 10% | fallback to degraded response mode |

## 6. Human Approval Workflows

AI may recommend actions, but high-impact actions must be approved by a human.

## Approval Matrix

| Action | Drafted By | Approval Required | Approver |
|--------|------------|-------------------|----------|
| Follow-up email draft | Email Agent | yes before sending | Sales/CS or Manager |
| Renewal discount suggestion | Recommendation Agent | yes | Manager |
| Support escalation | Recommendation Agent | yes | Manager or Admin |
| CRM field update | Meeting/Email Agent | yes | record owner |
| Customer health/risk recalculation | Risk Agent | no, but logged | system |
| External notification | Any agent | yes | Admin or Manager |

## Approval States

| State | Meaning |
|-------|---------|
| draft | AI generated but not visible externally |
| pending_review | waiting for human decision |
| approved | can be executed |
| rejected | cannot be executed |
| executed | completed by system/user |
| expired | stale and must be regenerated |

## 7. Disaster Recovery

## Recovery Objectives

| Component | RPO | RTO | Recovery Strategy |
|-----------|-----|-----|-------------------|
| TiDB structured data | 24 hours for demo, stricter for production | 4 hours | scheduled dumps or TiDB Cloud backups |
| Pinecone vectors | 24 hours | 4 hours | re-index from source documents and metadata |
| Source documents | 24 hours | 4 hours | object storage backup or repo-controlled synthetic data |
| Environment config | latest committed template | 1 hour | `.env.example` plus secure secret manager |
| ML artifacts | every approved version | 2 hours | model registry and artifact storage |
| Logs/audits | 24 hours | 4 hours | append-only export or database backup |

## Backup Checklist

- Export TiDB schema and data.
- Preserve source documents or synthetic generation seeds.
- Preserve Pinecone index configuration.
- Preserve model artifacts and evaluation outputs.
- Preserve `.env.example`; store real secrets outside git.
- Document restore commands in deployment notes.

## Recovery Drill

Run at least once before final demo:

1. Start from a clean environment.
2. Restore database schema and data.
3. Recreate Pinecone index.
4. Re-run embedding/indexing.
5. Start API.
6. Verify login, dashboard, AI query, analytics, graph, and admin logs.
7. Record recovery time and failures.

## 8. Governance Definition of Done

A feature touching data, AI, security, or business actions is done only when:

- role permissions are defined
- audit events are defined
- data classification is clear
- model/prompt version impact is checked
- observability metrics are listed
- rollback or recovery behavior is known
- human approval is defined for external or high-impact actions
