# 📓 Learning Log — Production Agentic RAG

> This file is my daily journal of what I built, what I learned, and what confused me.
> It is updated at the end of every coding session so AI can pick up context next time.

---

## How to use this file
- At the start of each session: AI reads this to understand where I am
- At the end of each session: I update the current day's entry
- Struggles are as important to record as wins — they show real learning

---

## Day 1 — Infrastructure & Project Setup
**Date:** 2026-09-02
**Status:** 🔄 In Progress

### What I Built
- [x] Project directory structure (`src/`, `airflow/`, `tests/`, `progress/`, etc.)
- [x] `.gitignore` — tells Git which files to NEVER commit (secrets, caches, IDE files)
- [x] `README.md` — project overview, architecture, setup guide
- [x] `LEARNING_LOG.md` — this file, for session-to-session memory
- [x] `CONCEPT_NOTES.md` — concepts explained in own words
- [x] `.env.example` — template of all environment variables (safe to commit)
- [x] `pyproject.toml` — full dependency list using uv
- [x] `src/__init__.py` and subpackage `__init__.py` files
- [x] GitHub repo created and pushed: https://github.com/Tanishqbot/production-agentic-learning
- [x] `src/config.py` — Settings class with pydantic-settings ✅
- [x] `src/database.py` — SQLAlchemy engine, SessionLocal, Base ✅
- [ ] `src/main.py` — FastAPI app + health endpoint
- [ ] `compose.yml` — Docker Compose
- [ ] First Alembic migration

### Concepts I Understood Today

**1. pydantic-settings / Settings class**
- `BaseSettings` reads values from a `.env` file automatically
- Each field in the class becomes a config variable
- If the `.env` has `POSTGRES_PORT=5433`, pydantic reads it and validates type
- If missing from `.env`, the `default` value is used
- `model_config = SettingsConfigDict(env_file=".env")` is a class-level variable (special Pydantic hook), NOT a nested class

**2. Layered Architecture**
- Router → Service → Repository → Database
- Each layer only talks to the one directly below it
- Makes code testable and swappable independently

**3. Why `__init__.py` files?**
- Makes Python treat a folder as a "package"
- Allows `from src.config import settings` style imports

**4. Why `.env.example` and not `.env`?**
- `.env` has real secrets — never commit it (in `.gitignore`)
- `.env.example` has fake placeholder values — safe to commit
- New developers copy `.env.example` to `.env` and fill in real values

**5. SQLAlchemy — database.py concepts**
- `create_engine(DATABASE_URL)` creates the connection pool to PostgreSQL
- `sessionmaker(autocommit=False, autoflush=False, bind=engine)` creates a session factory
  - `autocommit=False` → you control when data is committed (essential for rollback)
  - `autoflush=False` → SQLAlchemy won't secretly write to DB mid-request
- `declarative_base()` returns a class (`Base`) that all ORM models inherit from
- f-strings: `f"text {variable}"` — the `{}` is evaluated at runtime and inserted

**6. Python naming convention — classes use PascalCase**
- Classes: `Base`, `Settings`, `Paper`, `SessionLocal` (capital first letter)
- Variables/functions: `settings`, `engine`, `database_url` (snake_case)

### Mistakes Made and Corrections

**config.py mistakes:**
1. `Field(default="5432")` for int field → should be `Field(default=5432)` (no quotes)
2. `model_config` as a nested class → it's a class-level variable directly inside `Settings`
3. Unused import: `BaseModel` imported but never used

**database.py mistakes:**
1. Imported `Settings` (class) AND `settings` (instance) → only need `settings` instance
2. `f"postgresql://user:password@host:port/dbname"` — literal text, not f-string variables
   Correct: `f"postgresql://{settings.postgres_user}:{settings.postgres_password}@..."`
3. Named Base class `base` (lowercase) → should be `Base` (PascalCase — it's a class)
4. `sessionmaker(bind=engine)` missing `autocommit=False, autoflush=False`

### Questions Answered
- `case_sensitive=False` → makes `POSTGRES_HOST` and `postgres_host` map to same setting
- Why import `settings` not `Settings`? → We use the single ready-made instance
- Why `autocommit=False`? → Need control over transactions to allow rollbacks

### Next Task
`src/main.py` — FastAPI app entry point + `/health` endpoint

---

## Day 2 — Data Ingestion Pipeline
**Date:** _Not started yet_
**Status:** ⏳ Pending

### What I Built
- [ ] Airflow DAG for daily arXiv sync
- [ ] arXiv API fetcher (`httpx`)
- [ ] Docling PDF parser
- [ ] Text chunker with metadata
- [ ] SQLAlchemy models: `Paper`, `Chunk`
- [ ] Repository layer: save to DB

### Concepts I Understood Today
_Fill in after session_

### Things That Confused Me
_Fill in after session_

### Questions for Next Session
_Fill in after session_

---

## Day 3 — Embeddings + Hybrid Search
**Date:** _Not started yet_
**Status:** ⏳ Pending

### What I Built
- [ ] Jina AI embedding client (passage mode)
- [ ] Jina AI embedding client (query mode)
- [ ] OpenSearch index with `knn_vector` field
- [ ] BM25 keyword search
- [ ] Vector similarity search
- [ ] RRF fusion algorithm
- [ ] Context builder (Top-K chunks)

### Concepts I Understood Today
_Fill in after session_

### Things That Confused Me
_Fill in after session_

### Questions for Next Session
_Fill in after session_

---

## Day 4 — Agentic Layer + FastAPI Backend
**Date:** _Not started yet_
**Status:** ⏳ Pending

### What I Built
- [ ] Ollama LLM client (via LangChain)
- [ ] Prompt template
- [ ] Answer generator with sources
- [ ] LangGraph workflow (grade → retrieve → rewrite → generate)
- [ ] FastAPI: `POST /ask-agentic`
- [ ] FastAPI: `POST /stream`
- [ ] Redis caching middleware

### Concepts I Understood Today
_Fill in after session_

### Things That Confused Me
_Fill in after session_

### Questions for Next Session
_Fill in after session_

---

## Day 5 — Clients + Observability
**Date:** _Not started yet_
**Status:** ⏳ Pending

### What I Built
- [ ] Langfuse tracing integration
- [ ] Prompt versioning in Langfuse
- [ ] Gradio chat UI
- [ ] Telegram bot
- [ ] Final cleanup + README update

### Concepts I Understood Today
_Fill in after session_

### Things That Confused Me
_Fill in after session_

### Questions for Next Session
_Fill in after session_

---

## Overall Progress
- **Project started:** 2026-09-02
- **Last session:** 2026-09-02 — Day 1 (in progress)
- **Files written:** config.py ✅ | database.py ✅ | main.py ✅ (needs runtime verification)
- **Next task:** Verify `main.py` runs → then `compose.yml` → then Alembic migration
- **Blockers:** Docker Desktop not yet installed (needed for compose.yml and Alembic)
- **GitHub:** https://github.com/Tanishqbot/production-agentic-learning
- **AI Context file:** `AI_CONTEXT.md` — full project state + teaching instructions for any future AI
