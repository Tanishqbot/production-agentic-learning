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
- [x] `src/config.py` — Settings class with pydantic-settings ✅ (first code written!)
- [ ] `src/database.py` — SQLAlchemy engine
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

### Mistakes I Made (and corrections)
1. **Passing strings for int fields** — `Field(default="5432")` should be `Field(default=5432)`. No quotes for integers.
2. **`model_config` as a nested class** — It's a class-level variable directly inside `Settings`, not a separate class. Pydantic v2 treats `model_config` as a special reserved name.
3. **Unused import** — Imported `BaseModel` from pydantic but never used it. Removed.

### Things That Confused Me
- Why `model_config` is a class variable and not a regular class — will look at Pydantic v2 docs more

### Questions for Next Session
- What exactly is `case_sensitive=False` doing in `SettingsConfigDict`?
- Next task: `src/database.py`

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
- **Next task:** `src/database.py` — SQLAlchemy engine setup
- **Blockers:** Docker Desktop not yet installed (needed for Day 1 compose.yml)
- **GitHub:** https://github.com/Tanishqbot/production-agentic-learning
