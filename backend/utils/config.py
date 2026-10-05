# Configuration and embeddings
"""
ClientIQ — Configuration Management
Centralizes all environment variable loading and validation using Pydantic Settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # ── Application ──────────────────────────────────────────────────────────
    app_name: str = "ClientIQ"
    app_env: str = "development"
    app_secret_key: str = "change-me"
    app_debug: bool = True

    # ── TiDB ─────────────────────────────────────────────────────────────────
    tidb_host: str = "localhost"
    tidb_port: int = 4000
    tidb_user: str = "root"
    tidb_password: str = ""
    tidb_database: str = "clientiq"
    tidb_ssl: bool = False

    # ── Pinecone ─────────────────────────────────────────────────────────────
    pinecone_api_key: str = ""
    pinecone_environment: str = "us-east-1-aws"
    pinecone_index_name: str = "clientiq-docs"
    pinecone_upsert_batch_size: int = 25
    pinecone_request_timeout: int = 60

    # ── LLM ──────────────────────────────────────────────────────────────────
    llm_provider: str = "groq"
    groq_api_key: str = ""
    groq_base_url: str = "https://api.groq.com/openai/v1"
    groq_model: str = "llama-3.1-8b-instant"
    mistral_api_key: str = ""
    mistral_base_url: str = "https://api.mistral.ai/v1"
    mistral_model: str = "mistral-small-latest"

    # ── Embeddings ───────────────────────────────────────────────────────────
    embedding_model: str = "BAAI/bge-small-en-v1.5"
    embedding_dimension: int = 384

    # ── JWT ──────────────────────────────────────────────────────────────────
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 480

    # ── RAG ──────────────────────────────────────────────────────────────────
    chunk_size: int = 512
    chunk_overlap: int = 64
    top_k_results: int = 5

    # ── Logging ──────────────────────────────────────────────────────────────
    log_level: str = "INFO"
    log_file: str = "logs/clientiq.log"

    @property
    def tidb_url(self) -> str:
        """Construct SQLAlchemy connection URL for TiDB (MySQL-compatible)."""
        return (
            f"mysql+pymysql://{self.tidb_user}:{self.tidb_password}"
            f"@{self.tidb_host}:{self.tidb_port}/{self.tidb_database}"
        )

@lru_cache()
def get_settings() -> Settings:
    """Return cached singleton settings instance."""
    return Settings()


# Module-level shortcut for convenience
settings = get_settings()
