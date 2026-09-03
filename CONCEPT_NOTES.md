# 📚 Concept Notes — Production Agentic RAG

> Concepts explained in MY OWN WORDS after understanding them.
> Writing it in your own words is the real test of understanding.
> Updated throughout the 5-day build.

---

## Infrastructure & API Concepts

### What is `pydantic-settings` and why use it?

`pydantic-settings` solves the problem of app configuration. Every app needs settings like database passwords, API keys, and host addresses. You never hardcode these in your Python files (that would expose secrets on GitHub). Instead:

1. You put real secrets in a `.env` file (never committed to Git)
2. You create a `Settings` class that inherits from `BaseSettings`
3. Pydantic automatically reads the `.env` file and maps values to fields
4. If a value is missing from `.env`, the `default` is used
5. If a value has the wrong type (e.g. someone writes `PORT=abc`), Pydantic raises a validation error immediately on startup — not randomly mid-request

```
.env file  →  Settings class  →  settings.postgres_host used everywhere
```

It's like a typed, validated config object that loads itself from the environment.

### Why does `model_config` sit directly inside the class and NOT as a nested class?

`model_config` is a **class-level variable** in Pydantic v2. Pydantic looks for this specific name when the class is created and uses it to configure behavior. It's NOT a nested class — it's just a variable that holds a `SettingsConfigDict` object.

Think of it like this: Pydantic's `BaseSettings` is "listening" for a class variable named exactly `model_config`. When you define it:
```python
model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)
```
Pydantic picks it up and says "OK, read from `.env`, and ignore upper/lowercase differences in variable names."

If you make it a nested class (like `class model_config:`), Pydantic won't recognize it — it's looking for a variable, not a class.

### What does `case_sensitive=False` do?

It means `POSTGRES_HOST`, `postgres_host`, and `Postgres_Host` in your `.env` file all map to the same setting. This is important because environment variables on Linux/Mac are case-sensitive, but on Windows they're not. Setting `case_sensitive=False` makes your app work the same on both operating systems.

### What is `Field(default=...)` vs just `= value`?

Both work for simple defaults:
```python
# These two are identical in behavior
postgres_host: str = "localhost"
postgres_host: str = Field(default="localhost")
```

Use `Field()` when you need extras like:
- `description="The host address"` — for auto-generated API docs
- `alias="DB_HOST"` — if your `.env` uses a different name
- `ge=1, le=65535` — min/max validation for port numbers

For this project we use `Field()` for all settings as a consistent style, even if simple.

### What is the Repository Pattern?

In this project, code is split into layers:

```
Request → Router → Service → Repository → Database
```

The **Repository** layer is a class that only does one thing: talk to the database. It has methods like `get_paper_by_id()`, `save_paper()`, `list_papers()`. No business logic — just raw data operations.

The **Service** layer calls the repository. It decides *what* to do ("fetch the paper, then embed it, then index it") but doesn't know *how* the DB works.

**Why?** If you switch from PostgreSQL to MongoDB tomorrow, you only rewrite the Repository. The Service and Router don't need to change because they never directly touched the DB.

---

### What is Docker and why does this project use it?

Docker lets you run software in isolated containers. Instead of installing PostgreSQL, OpenSearch, and Redis directly on your Windows machine (which is painful and causes version conflicts), you define them in a `compose.yml` file and run:

```bash
docker compose up -d
```

Docker downloads the official images and runs them as if they were separate mini-computers. They're isolated, reproducible, and can be torn down with one command. Every developer on the team gets the exact same environment.

### What is Docker Compose?

`compose.yml` is a file that describes all the services your app needs. Instead of running 5 separate `docker run` commands, you describe them all in one file and start them together. It also handles networking between containers (your FastAPI app can reach `postgres:5432` inside Docker's network).

### What is FastAPI?

FastAPI is a Python web framework for building REST APIs. It has three superpowers:
1. **Speed** — async support makes it one of the fastest Python frameworks
2. **Auto validation** — if a request has wrong data types, FastAPI rejects it automatically using Pydantic
3. **Auto docs** — visit `/docs` and get a free interactive UI to test all endpoints

### What is `async/await` in FastAPI?

When your code calls a database or an external API, it has to *wait* for the response. In normal synchronous Python, this blocks the whole program — nothing else can run while waiting.

`async/await` changes this. When you `await db.get(paper_id)`, Python says "I'll wait for this, but in the meantime, handle other incoming requests." This makes your server handle many requests at once without needing multiple threads.

### What is SQLAlchemy (ORM)?

An ORM (Object-Relational Mapper) lets you interact with a database using Python objects instead of raw SQL strings.

Instead of:
```sql
INSERT INTO papers (title, url) VALUES ('My Paper', 'arxiv.org/1');
```

You write:
```python
paper = Paper(title="My Paper", url="arxiv.org/1")
session.add(paper)
session.commit()
```

Benefits:
- No SQL injection risk (ORM handles escaping)
- Python autocomplete for column names (no typos)
- Works with multiple DB types without changing your code

### What is a database migration (Alembic)?

Your database schema (table structure) changes over time. You add columns, rename things, add new tables. Alembic tracks these changes as numbered migration files — like Git commits for your database schema.

```
migrations/
  001_create_papers_table.py
  002_add_chunk_count_column.py
  003_create_chunks_table.py
```

Running `alembic upgrade head` applies all migrations in order. This means every developer and every server always has the exact same DB structure. If something goes wrong, you can roll back with `alembic downgrade -1`.

**How autogenerate works:**
Alembic's `env.py` is the brain of the migration system. It connects Alembic to YOUR models and YOUR database. Two critical things must be configured:

1. **`target_metadata = Base.metadata`** — without this, Alembic has no idea what your models look like. `Base.metadata` is SQLAlchemy's registry of every model that inherits from `Base`. Setting this lets Alembic compare the DB's actual schema against your model definitions and generate the difference as SQL.

2. **`config.set_main_option("sqlalchemy.url", DATABASE_URL)`** — by default Alembic reads the DB URL from `alembic.ini` (a static config file). We override it here so our dynamic `DATABASE_URL` (which reads from `.env` via settings) is used instead. One source of truth for the DB URL.

**The migration workflow:**
```
1. Write/change a model in src/models/
2. alembic revision --autogenerate -m "describe change"
   → Alembic compares your models to the DB → generates a .py file in versions/
3. Review the generated file (always check it's doing what you expect)
4. alembic upgrade head
   → Runs the SQL against your actual PostgreSQL DB
```

### What is a SQLAlchemy ORM Model?

A model is a Python class that represents a database table. Every class that inherits from `Base` becomes a table. The class name becomes the Python handle; `__tablename__` becomes the actual SQL table name.

```python
class Paper(Base):          # Paper = Python class name (PascalCase)
    __tablename__ = "papers"  # "papers" = actual PostgreSQL table name (snake_case)
```

**Column rules learned:**
- Column names: always **lowercase snake_case** — SQLAlchemy creates the column with the exact name you give
- `Integer + primary_key=True` → auto-increment implied, no need for `autoincrement=True`
- `nullable=False` → the DB rejects inserts that omit this field (enforced at DB level, not just Python)
- `unique=True` → DB creates a unique index, rejects duplicate values
- `index=True` → creates a DB index for faster lookups on that column (use on frequently-queried columns)

**Timezone-aware defaults — important Python 3.12 detail:**
```python
# DEPRECATED in Python 3.12 — returns naive datetime (no timezone info)
created_at = Column(DateTime, default=datetime.utcnow)

# CORRECT — returns timezone-aware datetime
created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
```

Why lambda? Without it, `datetime.now(timezone.utc)` would be evaluated **once** when Python loads the class definition — every row would get the same timestamp. The `lambda:` makes it a deferred call — evaluated fresh each time a row is inserted.



### What is Docker Compose and how does `compose.yml` work?

Docker Compose lets you define and run multiple Docker containers together using one YAML file. Instead of installing PostgreSQL, OpenSearch, Redis directly on your machine, you describe them in `compose.yml` and Docker runs them as isolated containers.

**The 6 key concepts:**

**1. Service** — one running container. The name you give it (e.g. `postgres`) becomes its hostname on the internal network. Other containers reach it by that name, not by `localhost`.

**2. `image`** — the pre-built Docker image to use, pulled from Docker Hub. Format: `name:version`. Example: `postgres:15` downloads PostgreSQL version 15.

**3. `ports`** — maps your machine's port to the container's port. Format: `"host:container"`. Always quote them. Example: `"5432:5432"` means traffic hitting your machine on 5432 goes into the container's 5432.

**4. `environment`** — passes config variables into the container. This is how you configure images without editing files inside them. Two valid formats:
```yaml
# List format (used here)
environment:
  - POSTGRES_USER=rag_user

# Map format (alternative)
environment:
  POSTGRES_USER: rag_user
```

**5. `volumes`** — without this, all data is lost when container stops. A named volume persists data outside the container. Format: `volume_name:/path/inside/container`. You declare named volumes at the bottom of the file.

**6. `networks`** — containers on the same network can reach each other by service name. `driver: bridge` is the default and correct choice for local development.

**Why `depends_on` alone is not enough:**
`depends_on: postgres` only waits for the postgres **container to start**, not for PostgreSQL to be **ready to accept connections**. PostgreSQL takes a few seconds to initialize. Without a healthcheck, Airflow tries to connect before PostgreSQL is ready and crashes.

Solution: add a `healthcheck` to postgres (uses `pg_isready` — PostgreSQL's own tool), then tell Airflow to wait for `condition: service_healthy` instead of just container started.

**`restart` policies:**
- `unless-stopped` — restart automatically on crash, but respect manual `docker compose down`
- `on-failure` — restart only if container exited with an error code (used for Airflow which may fail on first boot)

---


## Search & Embeddings Concepts

_(To be filled in after Day 3)_

### What is an embedding (vector representation)?
_Write your explanation here after Day 3_

### Why two Jina models: retrieval.passage vs retrieval.query?
_Write your explanation here after Day 3_

### What is BM25 (keyword search)?
_Write your explanation here after Day 3_

### What is Hybrid Search and RRF?
_Write your explanation here after Day 3_

---

## Agentic & LLM Concepts

_(To be filled in after Day 4)_

### What is LangGraph and what makes a system "agentic"?
_Write your explanation here after Day 4_

### What is streaming (SSE)?
_Write your explanation here after Day 4_

### What is Redis caching?
_Write your explanation here after Day 4_

---

## Observability & Clients

_(To be filled in after Day 5)_

### What is observability in production AI?
_Write your explanation here after Day 5_

### What is a Langfuse trace?
_Write your explanation here after Day 5_
