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
- [x] `src/main.py` — FastAPI app + /health + / endpoints ✅ (server verified running)
- [x] `compose.yml` — Docker Compose ✅ (all 4 services running and healthy)
- [x] `src/models/paper.py` — Paper ORM model ✅
- [x] Alembic init + first migration ✅ (`papers` table created and verified in PostgreSQL)

**Day 1 Status: ✅ COMPLETE**

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

**7. Docker Compose — compose.yml concepts**
- A `service` = one container. Service name becomes its internal hostname (not `localhost`)
- `image` = pre-built image from Docker Hub (`name:version`)
- `ports` = `"host:container"` — always quote! YAML can misparse unquoted ports
- `environment` = config passed into the container (list format: `- KEY=value`)
- `volumes` = persist data outside the container — without this all data lost on restart
- `networks` = shared network so containers talk to each other by service name
- `depends_on` alone only checks if container STARTED, not if service is READY
- `healthcheck` = tells Docker how to verify a service is actually ready
- `restart: unless-stopped` = auto-restart on crash (for stateful services)
- `restart: on-failure` = restart only on error exit (for Airflow which may fail on first boot)

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

**main.py mistakes:**
1. Missing commas between `FastAPI()` arguments → SyntaxError
2. `version=1.0.0` not quoted → SyntaxError (not a valid Python literal)
3. `def read_root()` instead of `async def` → inconsistent, should always be async

**compose.yml — improvements needed (not mistakes, but production gaps):**
1. Ports unquoted (`- 5432:5432`) → should be quoted (`- "5432:5432"`)
2. Missing `restart` policy on all services
3. `depends_on` uses list format → should use condition format with healthcheck
4. Missing `healthcheck` on postgres → Airflow connects before DB is ready

**paper.py mistakes:**
1. `Url` (capital U) → should be `url` (lowercase). Column names are always snake_case.
   SQLAlchemy creates the column exactly as named — `Url` creates a case-sensitive Postgres column
2. `autoincrement=True` is redundant → Integer + primary_key=True implies auto-increment

**paper.py — what the student did BETTER than suggested:**
- Used `default=lambda: datetime.now(timezone.utc)` instead of `datetime.utcnow`
- `datetime.utcnow()` is deprecated in Python 3.12 — returns naive (timezone-unaware) datetime
- `datetime.now(timezone.utc)` returns timezone-aware datetime — correct for production
- Lambda ensures the function is called fresh each insert, not once at import time

### Concepts I Understood Today (continued)

**8. SQLAlchemy ORM Models**
- A model = a Python class that maps to a DB table
- Must inherit from `Base` (from `src.database`)
- `__tablename__` sets the actual table name in PostgreSQL
- `Column(Type, options)` defines each column
- Column naming: always snake_case lowercase (matches DB convention)
- `primary_key=True` on Integer → auto-increment implied, no need for `autoincrement=True`
- `nullable=False` = required field (DB enforces this, not just Python)
- `unique=True` = DB enforces no duplicates on this column
- `default=lambda: datetime.now(timezone.utc)` = timezone-aware timestamp on insert

**9. Alembic — Database migrations**
- Alembic is version control for your database schema
- `alembic init src/db` → creates env.py, versions/, alembic.ini
- `target_metadata = Base.metadata` → tells Alembic which models to watch
- `config.set_main_option("sqlalchemy.url", DATABASE_URL)` → override URL from code, not .ini
- `alembic revision --autogenerate -m "message"` → generates migration by comparing models vs DB
- `alembic upgrade head` → applies all pending migrations to the DB
- `alembic downgrade -1` → rolls back last migration

**env.py changes made:**
1. Added `from src.database import Base, DATABASE_URL` at top
2. Changed `target_metadata = None` → `target_metadata = Base.metadata`
3. Added `config.set_main_option("sqlalchemy.url", DATABASE_URL)` after `config = context.config`

**alembic.ini change made:**
- Commented out / blanked `sqlalchemy.url` since it's now set dynamically in env.py

### Questions Answered
- `case_sensitive=False` → makes `POSTGRES_HOST` and `postgres_host` map to same setting
- Why import `settings` not `Settings`? → We use the single ready-made instance
- Why `autocommit=False`? → Need control over transactions to allow rollbacks
- Why quote ports in YAML? → YAML parses `5432:5432` ambiguously as a ratio, not a string
- Why `depends_on` needs healthcheck? → Container starting ≠ service being ready to connect
- Why is `Url` wrong? → SQLAlchemy uses the name literally; case-sensitive columns are a nightmare to query
- Why `datetime.now(timezone.utc)` over `datetime.utcnow`? → utcnow deprecated in 3.12, returns naive datetime
- Why lambda in default? → Without lambda, the expression evaluates ONCE at class definition time, not per-insert

### Next Task
Run `alembic revision --autogenerate -m "create papers table"` then `alembic upgrade head`

---


## Day 2 — Data Ingestion Pipeline
**Date:** 2026-09-04
**Status:** 🔄 In Progress

### What I Built
- [x] `src/models/chunk.py` — Chunk ORM model ✅ (fixed all 4 issues, relationship correct)
- [x] Second Alembic migration — create `chunks` table ✅ (verified in PostgreSQL)
- [ ] `src/dependencies.py` — FastAPI DB session injector
- [ ] `src/repositories/paper_repository.py` — DB queries for papers
- [ ] `src/repositories/chunk_repository.py` — DB queries for chunks
- [ ] `src/services/arxiv_fetcher.py` — fetch papers from arXiv API
- [ ] `airflow/dags/arxiv_sync.py` — daily Airflow DAG

### Concepts I Understood Today

**1. Alembic `include_name` filter — critical for shared databases**
- Airflow and our app share the same PostgreSQL DB (`rag_db`)
- Airflow creates its own `ab_*` tables (Flask App Builder tables)
- Without a filter, Alembic autogenerate sees those tables, thinks they shouldn't exist, and generates DROP TABLE statements — destroying Airflow's data
- Fix: add `include_name` function to `env.py` that returns `True` only for tables in `Base.metadata`
- Rule: Alembic should ONLY manage tables it created — ignore everything else

**2. Foreign Keys — linking tables together**
- A foreign key is a column that points to a primary key in another table
- `ForeignKey("papers.id")` = "this value must exist as an `id` in the `papers` table"
- The DB enforces this: you can't create a chunk for a non-existent paper (integrity constraint)
- SQLAlchemy syntax: `Column(Integer, ForeignKey("table_name.column_name"), nullable=False)`

**3. SQLAlchemy Relationships — Python-level navigation**
- `relationship()` is a Python-level shortcut — it does NOT create a DB column
- It lets you navigate between objects: `paper.chunks` → list of chunks, `chunk.paper` → the parent paper
- The 3 rules of `relationship()`:
  - **Attribute name** = what you GET (`chunks` → list of chunks, `paper` → one paper)
  - **String argument** = the OTHER model's class name (exact PascalCase)
  - **`back_populates`** = attribute name on the OTHER side (must match exactly, bidirectional)

```
Paper.chunks = relationship("Chunk", back_populates="paper")
Chunk.paper  = relationship("Paper", back_populates="chunks")
```

**4. One-to-Many relationship pattern**
- One Paper has MANY Chunks → Paper side gets a list attribute (plural name: `chunks`)
- One Chunk belongs to ONE Paper → Chunk side gets a single object attribute (singular: `paper`)
- The foreign key (`paper_id`) lives on the MANY side (Chunk), not the ONE side (Paper)

### Mistakes Made and Corrections

**Alembic (env.py) — initial setup:**
- Missing `include_name` filter → autogenerate tried to DROP Airflow tables
- Fix: add function `include_name(name, type_, parent_names)` that filters by `target_metadata.tables`
- Add `include_name=include_name` to both `context.configure()` calls in env.py

**chunk.py mistakes:**
1. `class chunk` (lowercase) → `class Chunk` (PascalCase — it's a class) ← recurring mistake
2. Column named `context` → should be `content` (context is a framework keyword)
3. `autoincrement=True` on `chunk_index` → removed (only meaningful for primary keys)
4. Relationship: `chunk = relationship("Chunk", back_populates="paper")` → 3 sub-errors:
   - Variable `chunk` → should be `paper` (you get a paper from a chunk)
   - `"Chunk"` → should be `"Paper"` (point to the OTHER model)
   - `back_populates="paper"` → should be `"chunks"` (attr name on Paper)

**paper.py mistakes:**
1. `Url` (capital) → `url` ← SAME mistake as Day 1, not fixed
2. `paper = relationship("Paper", ...)` → 2 sub-errors:
   - Variable `paper` → should be `chunks` (you get chunks from a paper)
   - `"Paper"` → should be `"Chunk"` (self-referential is wrong)

### Questions Answered
- Why does Alembic try to drop Airflow tables? → It sees DB tables not in metadata → thinks they're orphans to delete
- What is `back_populates`? → Tells SQLAlchemy the name of the matching attr on the other side (bidirectional)
- Why is the FK on the Chunk side, not Paper? → FK always goes on the MANY side of a one-to-many
- Why PascalCase for class name matters in relationships? → SQLAlchemy string lookup `"Chunk"` must match class name exactly

### Next Task
Apply all 6 fixes to chunk.py and paper.py → run second Alembic migration

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
