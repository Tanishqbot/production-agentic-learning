from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    """
    Central configuration for the entire application.
    Values are loaded from the .env file automatically.
    If a variable is missing from .env, the default value is used.
    """

    # model_config is a special Pydantic v2 class variable — NOT a nested class.
    # It tells pydantic-settings: "read values from .env, ignore case differences"
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

    # ------------------------------------------------------------------
    # PostgreSQL — our relational database (stores paper metadata)
    # ------------------------------------------------------------------
    postgres_host: str = Field(default="localhost")
    postgres_port: int = Field(default=5432)
    postgres_user: str = Field(default="rag_user")
    postgres_password: str = Field(default="password")
    postgres_db: str = Field(default="rag_db")

    # ------------------------------------------------------------------
    # OpenSearch — our search engine (BM25 + vector search)
    # ------------------------------------------------------------------
    opensearch_host: str = Field(default="localhost")
    opensearch_port: int = Field(default=9200)

    # ------------------------------------------------------------------
    # Redis — our caching layer (avoid re-running expensive searches)
    # ------------------------------------------------------------------
    redis_host: str = Field(default="localhost")
    redis_port: int = Field(default=6379)

    # ------------------------------------------------------------------
    # Jina AI — our embedding API (converts text to vectors)
    # ------------------------------------------------------------------
    jina_api_key: str = Field(default="")

    # ------------------------------------------------------------------
    # Ollama — our local LLM (generates answers from retrieved context)
    # ------------------------------------------------------------------
    ollama_base_url: str = Field(default="http://localhost:11434")
    ollama_model: str = Field(default="llama3.2")

    # ------------------------------------------------------------------
    # Retrieval settings
    # ------------------------------------------------------------------
    retrieval_top_k: int = Field(default=5)


# A single shared instance used across the entire application.
# Other files do: from src.config import settings
settings = Settings()
