from backend.services.mistral_client import MistralClient
from backend.utils.config import Settings


def test_default_llm_provider_is_groq():
    settings = Settings()

    assert settings.llm_provider == "groq"
    assert settings.groq_base_url == "https://api.groq.com/openai/v1"
    assert settings.groq_model


def test_llm_client_uses_groq_defaults():
    client = MistralClient()

    assert client.provider == "groq"
    assert client.base_url == "https://api.groq.com/openai/v1"
    assert client.model
