from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.config import settings  # the single shared settings instance

# Build the PostgreSQL connection URL from our settings.
# Format: postgresql://user:password@host:port/database_name
# All values come from .env (via the Settings class) — no hardcoding.
DATABASE_URL = (
    f"postgresql://{settings.postgres_user}:{settings.postgres_password}"
    f"@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}"
)

# The engine is the core connection pool to PostgreSQL.
# It manages multiple simultaneous connections under the hood.
engine = create_engine(DATABASE_URL)

# SessionLocal is a factory for creating database sessions.
# Each request in FastAPI gets its own session (opened and closed per request).
# autocommit=False → we decide when to commit (gives us rollback control)
# autoflush=False  → we decide when to flush pending writes to the DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is the parent class all ORM models will inherit from.
# Pydantic convention: classes use PascalCase (Base, not base)
# When we define: class Paper(Base): ...
# SQLAlchemy knows it's a database model and maps it to a table.
Base = declarative_base()
