from pathlib import Path

from backend.api.main import app


ROOT = Path(__file__).resolve().parents[1]


def test_app_version_matches_version_sync():
    version_sync = (ROOT / "docs" / "VERSION_SYNC.md").read_text(encoding="utf-8")

    assert app.version == "1.0.0"
    assert "| API version | 1.0.0 |" in version_sync


def test_core_routes_are_registered():
    paths = {route.path for route in app.routes}

    assert "/api/health" in paths
    assert "/api/auth/login" in paths
    assert "/api/query/" in paths
    assert "/api/analytics/overview" in paths
    assert "/api/clients/" in paths
    assert "/api/graph/" in paths
    assert "/api/admin/audit-logs" in paths


def test_env_example_contains_settings_contract():
    env_example = (ROOT / ".env.example").read_text(encoding="utf-8")

    required_keys = [
        "APP_NAME",
        "APP_ENV",
        "APP_SECRET_KEY",
        "TIDB_HOST",
        "TIDB_PORT",
        "PINECONE_API_KEY",
        "PINECONE_INDEX_NAME",
        "GROQ_API_KEY",
        "GROQ_MODEL",
        "EMBEDDING_MODEL",
        "JWT_ALGORITHM",
        "CHUNK_SIZE",
        "TOP_K_RESULTS",
        "LOG_LEVEL",
    ]

    for key in required_keys:
        assert f"{key}=" in env_example
