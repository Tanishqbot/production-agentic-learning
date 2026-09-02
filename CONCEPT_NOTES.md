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
