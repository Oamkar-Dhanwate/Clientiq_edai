from backend.graph.router import classify_intent, get_required_agents


def test_classify_intent_for_core_business_queries():
    cases = {
        "Which client has the highest revenue?": "crm_query",
        "Find meeting notes for API integration issues": "document_search",
        "Show customers at high churn risk": "risk_analysis",
        "What action should we take next?": "recommendation",
        "Show dashboard KPI trend": "analytics",
        "Show knowledge graph relationship for Acme": "knowledge_graph",
    }

    for query, expected in cases.items():
        assert classify_intent(query) == expected


def test_required_agents_always_have_citation_for_answerable_intents():
    answerable_intents = [
        "crm_query",
        "document_search",
        "sentiment_check",
        "risk_analysis",
        "recommendation",
        "analytics",
        "knowledge_graph",
        "general_qa",
        "conversation",
    ]

    for intent in answerable_intents:
        assert "citation_agent" in get_required_agents(intent)


def test_unknown_intent_falls_back_to_general_qa_agents():
    assert get_required_agents("unknown") == get_required_agents("general_qa")
