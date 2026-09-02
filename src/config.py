from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, BaseModel

class Settings(BaseSettings):
    """ 
    Central config for the entire application
    Values are loaded from the .env file automatically
    If a variable is missing from the .env, default values are used
    """

    # PostgreSQL stores the paper metadata
    postgres_host: str = Field(default = "localhost")
    postgres_port: int = Field(default = 5432)
    postgres_user: str = Field(default = "rag_user")
    postgres_password: str = Field(default = "password")
    postgres_db: str = Field(default = "rag_db")

    # Opensearch is the search engine (BM25 + vector Search)
    opensearch_host: str = Field(default = "localhost")
    opensearch_port: int = Field(default = 9200)

    # Redis is the caching layer to avoing re-running searches
    redis_host: str = Field(default = "localhost")
    redis_port: int = Field(default = 6379)

    # Jina AI is the embedding API
    jina_api_key: str = Field(default = "")

    # For local LLM
    ollama_base_url: str = Field(default = "http://localhost:11434")
    ollama_model: str = Field(default = "llama3.2")

    # Retrieval settings
    retrieval_top_k: int = Field(default = 5)



    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

settings = Settings()

