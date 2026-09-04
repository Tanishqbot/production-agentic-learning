# 🤖 AI CONTEXT FILE — Production Agentic RAG Learning Project
### *Read this file completely before responding to any message in this session.*

---

## ⚠️ CRITICAL INSTRUCTIONS FOR THE NEXT AI

This student is building a **Production Agentic RAG system from scratch as a learning project**.
Your job is to **teach concepts and review code — NOT write code for the student**.

**The single most important rule:**
> You NEVER write complete working code and hand it to the student to copy.
> You explain what the code must do in plain English, the student writes it, then you review it.

Read this entire file before responding. The student will ask you to continue where the previous AI left off.

---

## 1. PROJECT OVERVIEW

**What is being built:**
An arXiv Paper Curator — a production-grade Agentic RAG (Retrieval-Augmented Generation) system that:
- Fetches academic papers from arXiv daily via Apache Airflow
- Parses PDFs with Docling
- Stores metadata in PostgreSQL, indexes in OpenSearch
- Embeds text with Jina AI (separate models for passage vs query)
- Retrieves with Hybrid Search (BM25 + vector) fused via RRF (Reciprocal Rank Fusion)
- Generates answers using a local LLM via Ollama + LangChain
- Has an Agentic layer using LangGraph (document grading, query rewriting, guardrails)
- Exposes a FastAPI REST backend with streaming
- Has a Telegram bot + Gradio chat UI
- Uses Langfuse for observability and Redis for caching

**Reference repo (DO NOT share code from this with student):**
https://github.com/jamwithai/production-agentic-rag-course

**Student's learning repo:**
https://github.com/Tanishqbot/production-agentic-learning

**Local project path:**
`D:\AI PLANET\production-agentic-rag\`

---

## 2. STUDENT PROFILE

| Attribute | Value |
|-----------|-------|
| Name | Tanishq Tembhurne |
| Python level | Intermediate — knows functions, loops, classes, basic OOP |
| Experience with async | Basic understanding |
| Docker status | NOT YET INSTALLED (needs to be done) |
| LLM choice | Local Ollama |
| Scope | Full project: backend + Telegram bot + Gradio UI |
| Goal | Finish in 5 days |
| Git | Configured (username: Tanishq Tembhurne, email: tanishqwork1310@gmail.com) |
| Tools installed | Python 3.12.7 ✅, git 2.43 ✅, uv 0.5.24 ✅, Docker ❌ |

---

## 3. TEACHING METHODOLOGY — FOLLOW THIS EXACTLY

This is how the previous AI taught. You must follow the same pattern precisely.

### 3.1 The Learning Contract (state this to student if they ask)

```
1. AI explains the concept using plain English + a real-world analogy
2. Student asks questions until concept is 100% clear
3. AI describes WHAT the code needs to do in plain English bullets (no code)
4. Student writes the code themselves
5. Student pastes their code → AI reviews line by line
6. AI explains every mistake — what's wrong, why it's wrong, what the correct version is
7. AI writes the corrected file (since student already tried)
8. Learnings are saved to LEARNING_LOG.md and CONCEPT_NOTES.md
9. Committed to GitHub (student commits themselves when possible)
```

### 3.2 Explanation Style

**Always explain concepts BEFORE giving the task.**
Use this structure for every concept:
1. **The Problem** — what problem does this solve?
2. **The Mental Model** — a real-world analogy
3. **The Why** — why this specific tool/pattern and not something else?
4. **Code-level detail** — only after the above

Example of good explanation (pydantic-settings):
> "The problem: your app needs secrets. Hardcoding them gets them committed to GitHub. Using `os.environ.get()` everywhere is messy and untyped. pydantic-settings solves this with a single `Settings` class that reads `.env`, validates types, and gives you autocomplete. Think of it like a typed config object that loads itself from the environment."

### 3.3 Code Task Format

When giving a coding task, always provide:
- What the file needs to DO (plain English bullets)
- Imports the student will need (just the import lines, nothing else)
- One or two syntax hints for patterns they haven't seen before
- "Hints if you get stuck" section at the bottom

Never provide:
- Function signatures pre-written
- The actual logic
- Complete code blocks to fill in

### 3.4 Code Review Format

When student submits code, always structure your review as:

```
## 🔍 Code Review

### ❌ Bug 1 (Critical/Minor): [title]
[their code snippet — wrong]
[explanation of WHY it's wrong]
[correct version]

### ⚠️ Style Issue: [title]
[explanation]

### ✅ What you got RIGHT
[list of correct things — always acknowledge what they did well]

## Score: X/100 → after correction: 100/100
```

### 3.5 End of Every Task

After the student writes a file:
1. Write the corrected version to the actual file path
2. Update `LEARNING_LOG.md` with:
   - What was built (check it off)
   - New concepts learned
   - Mistakes made + corrections
3. Update `CONCEPT_NOTES.md` with detailed explanations
4. Ask student to commit (they do it themselves, or AI commits if student asks)

### 3.6 Tone Rules

- **Never condescending** — mistakes are expected and good
- **Always explain the WHY** — never say "just do X" without explaining why
- **Acknowledge correct things first** then corrections
- **Use tables and code blocks** for clarity
- **Short paragraphs** — student reads on screen, not on paper
- **Emoji sparingly** — 🚀 ✅ ❌ ⚠️ are fine, don't overdo it

---

## 4. PROJECT FILE STRUCTURE

```
D:\AI PLANET\production-agentic-rag\
├── src/
│   ├── __init__.py
│   ├── config.py           ✅ DONE
│   ├── database.py         ✅ DONE
│   ├── main.py             ✅ DONE (needs verification)
│   ├── dependencies.py     ❌ NOT DONE YET
│   ├── exceptions.py       ❌ NOT DONE YET
│   ├── middlewares.py      ❌ NOT DONE YET
│   ├── gradio_app.py       ❌ NOT DONE YET (Day 5)
│   ├── models/
│   │   └── __init__.py     ✅ exists (empty)
│   ├── schemas/
│   │   └── __init__.py     ✅ exists (empty)
│   ├── routers/
│   │   └── __init__.py     ✅ exists (empty)
│   ├── services/
│   │   └── __init__.py     ✅ exists (empty)
│   ├── repositories/
│   │   └── __init__.py     ✅ exists (empty)
│   └── db/
│       └── __init__.py     ✅ exists (empty)
├── airflow/
│   └── dags/
│       └── .gitkeep        ✅ exists
├── notebooks/
│   └── .gitkeep            ✅ exists
├── tests/
│   └── __init__.py         ✅ exists (empty)
├── static/
│   └── .gitkeep            ✅ exists
├── progress/
│   ├── day1_summary.md     ✅ exists (placeholder)
│   ├── day2_summary.md     ✅ exists (placeholder)
│   ├── day3_summary.md     ✅ exists (placeholder)
│   ├── day4_summary.md     ✅ exists (placeholder)
│   └── day5_summary.md     ✅ exists (placeholder)
├── .gitignore              ✅ DONE
├── .env.example            ✅ DONE
├── README.md               ✅ DONE
├── LEARNING_LOG.md         ✅ maintained throughout
├── CONCEPT_NOTES.md        ✅ maintained throughout
├── AI_CONTEXT.md           ✅ THIS FILE
├── compose.yml             ✅ DONE (all 4 services running and healthy)
├── alembic.ini             ✅ DONE (sqlalchemy.url blanked, set dynamically in env.py)
└── pyproject.toml          ✅ DONE
```

---

## 5. CURRENT FILE CONTENTS (exact state)

### `src/config.py` — ✅ DONE
```python
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, BaseModel  # NOTE: BaseModel is unused import — minor issue

class Settings(BaseSettings):
    """
    Central config for the entire application
    Values are loaded from the .env file automatically
    If a variable is missing from the .env, default values are used
    """

    # PostgreSQL stores the paper metadata
    postgres_host: str = Field(default="localhost")
    postgres_port: int = Field(default=5432)
    postgres_user: str = Field(default="rag_user")
    postgres_password: str = Field(default="password")
    postgres_db: str = Field(default="rag_db")

    # Opensearch is the search engine (BM25 + vector Search)
    opensearch_host: str = Field(default="localhost")
    opensearch_port: int = Field(default=9200)

    # Redis is the caching layer to avoid re-running searches
    redis_host: str = Field(default="localhost")
    redis_port: int = Field(default=6379)

    # Jina AI is the embedding API
    jina_api_key: str = Field(default="")

    # For local LLM
    ollama_base_url: str = Field(default="http://localhost:11434")
    ollama_model: str = Field(default="llama3.2")

    # Retrieval settings
    retrieval_top_k: int = Field(default=5)

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

settings = Settings()
```

### `src/database.py` — ✅ DONE
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.config import settings

DATABASE_URL = (
    f"postgresql://{settings.postgres_user}:{settings.postgres_password}"
    f"@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}"
)

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
```

### `src/main.py` — ✅ DONE (student wrote, applied fixes)
```python
from fastapi import FastAPI

app = FastAPI(
    title="Production Agentic RAG",
    description="A research assistant that fetches arXiv papers and answers "
                "questions using Hybrid Search + local LLM.",
    version="1.0.0",
)

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "production-agentic-rag"}

@app.get("/")
async def read_root():
    return {
        "app": "Production Agentic RAG",
        "version": "1.0.0",
        "status": "running",
        "docs": "Visit /docs for interactive API documentation",
    }
```
**Verified:** `uv run uvicorn src.main:app --reload` → http://localhost:8000/health works ✅

### `compose.yml` — ✅ DONE
All 4 services verified running and healthy: postgres, opensearch, redis, airflow.
Student applied all 5 improvements independently (quoted ports, restart policies, healthcheck, condition depends_on).

### `src/models/paper.py` — 🔄 WRITTEN, ONE FIX PENDING
Student needs to change `Url` → `url`. Then run alembic.

Current student code (after fix will be):
```python
from sqlalchemy import Column, String, Integer, DateTime, Text
from datetime import datetime, timezone
from src.database import Base

class Paper(Base):
    __tablename__ = "papers"
    id = Column(Integer, primary_key=True, index=True)
    arxiv_id = Column(String(50), unique=True, nullable=False)
    title = Column(String(500), nullable=False)
    authors = Column(Text, nullable=True)
    abstract = Column(Text, nullable=True)
    url = Column(String(300), nullable=True)
    published_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
```
NOTE: Student used `lambda: datetime.now(timezone.utc)` — better than `datetime.utcnow` (deprecated in 3.12). Acknowledge this.

### `src/db/env.py` — ✅ DONE (3 changes applied by student)
Key changes from default Alembic template:
1. `from src.database import Base, DATABASE_URL` added at top
2. `target_metadata = Base.metadata` (was `None`)
3. `config.set_main_option("sqlalchemy.url", DATABASE_URL)` after `config = context.config`

### `alembic.ini` — ✅ DONE
`sqlalchemy.url` line blanked — URL now set dynamically in env.py

**CURRENT STATUS:** Student is about to run:
```bash
alembic revision --autogenerate -m "create papers table"
alembic upgrade head
```

---

## 6. MISTAKES THE STUDENT MADE (patterns to watch for)

These are recurring patterns this student makes. Watch for them in future code:

| Mistake | Example | Correction |
|---------|---------|-----------|
| String for int default | `Field(default="5432")` | `Field(default=5432)` |
| Nested class instead of class variable | `class model_config(): model_config = ...` | `model_config = SettingsConfigDict(...)` directly in class |
| Unused imports | `from pydantic import Field, BaseModel` | Remove `BaseModel` |
| Duplicate imports (class + instance) | `from src.config import Settings` AND `from src.config import settings` | Only import what you use |
| Literal text in f-string | `f"host:port/db"` | `f"{settings.host}:{settings.port}/{settings.db}"` |
| lowercase class names | `base = declarative_base()` | `Base = declarative_base()` |
| Missing commas in function calls | `FastAPI(title="x" description="y")` | `FastAPI(title="x", description="y")` |
| Non-string version | `version=1.0.0` | `version="1.0.0"` |
| Missing `async` on route handlers | `def read_root():` | `async def read_root():` |
| Uppercase column name | `Url = Column(...)` | `url = Column(...)` — columns always lowercase snake_case |
| Redundant autoincrement | `Column(Integer, autoincrement=True, primary_key=True)` | `Column(Integer, primary_key=True)` — implied |
| Lowercase class name | `class chunk(Base)` | `class Chunk(Base)` — classes always PascalCase |
| Wrong relationship direction | `relationship("Chunk", ...)` inside Chunk | Must point to OTHER model: `relationship("Paper", ...)` |
| Wrong attribute name | `chunk = relationship(...)` in Chunk class | Name = what you GET: `paper = relationship(...)` |
| Wrong back_populates | `back_populates="paper"` on Paper side | Must match attr name on OTHER side: `back_populates="chunks"` |
| Non-PK autoincrement | `chunk_index = Column(Integer, autoincrement=True)` | Remove — autoincrement only for primary keys |

---

## 7. CONCEPTS ALREADY EXPLAINED (DO NOT RE-EXPLAIN UNLESS ASKED)

The student has already understood these concepts. Don't re-explain unless they ask:

- What is pydantic-settings and BaseSettings
- What is `model_config` and why it's a class variable not a nested class
- What is `case_sensitive=False` in SettingsConfigDict
- What is `Field(default=...)` vs plain `= value`
- What is the Repository Pattern (Router → Service → Repository → DB)
- What is Docker and Docker Compose
- What is SQLAlchemy ORM
- What is `create_engine`, `sessionmaker`, `declarative_base`
- What is `autocommit=False` and `autoflush=False`
- What is `declarative_base()` and why models inherit from `Base`
- What are f-strings and how `{}` works in them
- What are `__init__.py` files and why they make packages
- Why `.env` is never committed and `.env.example` is
- What is a database migration (Alembic)
- What is FastAPI
- What is `async def` vs `def` in route handlers
- What is `@app.get()` decorator and how decorators work
- What is a health endpoint and why it matters in production
- Python naming conventions: PascalCase for classes, snake_case for variables

---

## 8. REMAINING WORK — 5-DAY PLAN

### Day 1 — Infrastructure (IN PROGRESS)
**Completed:**
- [x] Full project structure + GitHub repo
- [x] .gitignore, README.md, LEARNING_LOG.md, CONCEPT_NOTES.md
- [x] .env.example, pyproject.toml
- [x] src/config.py
- [x] src/database.py
- [x] src/main.py

**Still to do on Day 1:**
- [ ] BLOCKER: Install Docker Desktop → https://www.docker.com/products/docker-desktop/
- [ ] Verify main.py works: `uv run uvicorn src.main:app --reload` → hit http://localhost:8000/health
- [ ] compose.yml — Docker Compose for all services
- [ ] Alembic init + first migration (create papers table)

### Day 2 — Data Ingestion Pipeline
- [ ] Airflow DAG: daily arXiv sync
- [ ] arXiv API fetcher using httpx
- [ ] Docling PDF parser
- [ ] Text chunker with metadata
- [ ] SQLAlchemy models: Paper, Chunk in src/models/
- [ ] Repository layer: save to DB in src/repositories/

### Day 3 — Embeddings + Hybrid Search
- [ ] Jina AI client: passage embedding (for indexing)
- [ ] Jina AI client: query embedding (for search)
- [ ] OpenSearch index creation with knn_vector field
- [ ] BM25 keyword search function
- [ ] Vector similarity search function
- [ ] RRF fusion algorithm (~15 lines pure Python)
- [ ] Context builder: Top-K chunk selector

### Day 4 — Agentic Layer + Full API
- [ ] Ollama LLM client via langchain-ollama
- [ ] Prompt template
- [ ] Answer generator with sources + metadata
- [ ] LangGraph workflow: retrieve → grade → rewrite → generate
- [ ] FastAPI: POST /ask-agentic endpoint
- [ ] FastAPI: POST /stream endpoint (streaming SSE)
- [ ] Redis caching middleware

### Day 5 — Clients + Observability
- [ ] Langfuse trace integration
- [ ] Prompt versioning in Langfuse
- [ ] Gradio chat UI (src/gradio_app.py)
- [ ] Telegram bot
- [ ] Final cleanup + full README update

---

## 9. TECH STACK REFERENCE

| Layer | Technology | Why |
|-------|-----------|-----|
| Data source | arXiv API | Free academic papers |
| PDF parsing | Docling | State-of-art document understanding |
| Pipeline orchestration | Apache Airflow | Production-grade scheduling (DAGs) |
| Passage embeddings | Jina AI `retrieval.passage` | Optimized for indexing documents |
| Query embeddings | Jina AI `retrieval.query` | Optimized for search queries |
| Search + vector DB | OpenSearch | BM25 + kNN vector in one system |
| Metadata store | PostgreSQL + SQLAlchemy | Relational data (paper info, chunks) |
| Fusion algorithm | RRF (Reciprocal Rank Fusion) | Combines BM25 and vector rankings |
| LLM | Ollama (local) | Free, private, llama3.2 model |
| Agentic orchestration | LangGraph | State machine with decision nodes |
| LLM framework | LangChain + langchain-ollama | LLM abstraction layer |
| API | FastAPI | Async, auto-docs, type-safe |
| Caching | Redis | In-memory cache for repeated queries |
| Observability | Langfuse | Traces, prompt versioning |
| Telegram bot | python-telegram-bot | Mobile interface |
| Web UI | Gradio | Quick Python-native chat UI |
| Package manager | uv | Fast pip replacement |
| Container | Docker + Docker Compose | All services in containers |

---

## 10. GITHUB COMMIT CONVENTION USED IN THIS PROJECT

Format: `type(scope): short description`

Types:
- `feat` — new feature/file
- `fix` — bug fix
- `chore` — setup, config, non-code
- `docs` — documentation only
- `refactor` — code restructure without behavior change

Examples used:
```
chore: initial project scaffold
feat(day1): write src/config.py — Settings class with pydantic-settings
feat(day1): write src/database.py — SQLAlchemy engine setup
feat(day1): write src/main.py — FastAPI app with health and root endpoints
```

---

## 11. HOW TO CONTINUE THIS SESSION

When the student talks to you, do this first:

1. Read this file completely ✅ (you're doing this now)
2. Check what's next from Section 8 (Remaining Work)
3. Ask the student what they want to do:
   - Continue from where they left off (compose.yml + Docker)
   - Ask a concept question
   - Review code they wrote offline

**The immediate next task** (as of this file being written):
1. Verify `src/main.py` works by running uvicorn and hitting `/health`
2. Install Docker Desktop if not done
3. Write `compose.yml` — Docker Compose file

**When student is ready for compose.yml**, explain these concepts first:
- What Docker is (containers vs VMs)
- What Docker Compose is (orchestrating multiple containers)
- Why this project uses Docker (reproducibility, isolation)
- What each service does (postgres, opensearch, redis, airflow)

Then give them the task to write it.

---

## 12. ENVIRONMENT VARIABLES REFERENCE

All variables and their defaults (from .env.example):

```
OPENSEARCH_HOST=localhost
OPENSEARCH_PORT=9200
OPENSEARCH_USER=admin
OPENSEARCH_PASSWORD=your_opensearch_password_here
OPENSEARCH_INDEX_NAME=arxiv_papers

POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=rag_user
POSTGRES_PASSWORD=your_postgres_password_here
POSTGRES_DB=rag_db

REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=

JINA_API_KEY=your_jina_api_key_here

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2

LANGFUSE_PUBLIC_KEY=your_langfuse_public_key_here
LANGFUSE_SECRET_KEY=your_langfuse_secret_key_here
LANGFUSE_HOST=http://localhost:3000

TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here

APP_ENV=development
APP_HOST=0.0.0.0
APP_PORT=8000
LOG_LEVEL=INFO

RETRIEVAL_TOP_K=5
CHUNK_SIZE=512
CHUNK_OVERLAP=50
```

---

## 13. SESSION HISTORY SUMMARY

**Session 1 — 2026-09-02:**
- Student shared architecture diagram of the project
- AI explored the reference GitHub repo and extracted real file structure
- Created 5-day learning roadmap
- Student answered: Python=Intermediate, Docker=needs install, LLM=Ollama, Scope=full
- Set up full project structure locally
- Created GitHub repo: https://github.com/Tanishqbot/production-agentic-learning
- Pushed initial scaffold commit
- Student wrote `src/config.py` (first code!) — 3 mistakes corrected
- Student wrote `src/database.py` — 4 mistakes corrected
- Student wrote `src/main.py` — 3 mistakes corrected (commas, version string, async)
- Student was asked to commit main.py themselves and verify server works
- Student requested this context file

**Key teaching moments:**
- `model_config` is a class variable not a nested class (Pydantic v2 pattern)
- Strings vs integers in Field defaults
- f-string interpolation vs literal text
- PascalCase for classes, snake_case for variables
- Why `autocommit=False` matters
- Layered architecture (Router → Service → Repository → DB)
- Decorators in FastAPI (`@app.get()`)

---
*Last updated: 2026-09-02 | By: Antigravity AI*
*Next AI: Read Section 11 "How to Continue" for immediate next steps.*
