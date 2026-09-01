# 🤖 Production Agentic RAG — arXiv Paper Curator

> A production-grade Agentic RAG system that fetches academic papers from arXiv, understands their content, and answers research questions using hybrid search + local LLM.

**Built from scratch as a learning project. Every line of code written by hand.**

---

## Architecture

![Architecture Diagram](static/architecture.png)

**Tech Stack:**
| Layer | Technology |
|-------|-----------|
| Data Source | arXiv API |
| Parsing | Docling |
| Orchestration | Apache Airflow |
| Embeddings | Jina AI (passage + query) |
| Search | OpenSearch (BM25 + vector, fused via RRF) |
| Metadata Store | PostgreSQL + SQLAlchemy |
| Agentic Layer | LangGraph |
| LLM | Ollama (local) |
| API | FastAPI |
| Cache | Redis |
| Observability | Langfuse |
| Telegram Bot | python-telegram-bot |
| Web UI | Gradio |

---

## Project Structure

```
production-agentic-rag/
├── src/                    ← All application source code
│   ├── main.py             ← FastAPI app entry point
│   ├── config.py           ← Settings (pydantic-settings)
│   ├── database.py         ← PostgreSQL connection
│   ├── dependencies.py     ← FastAPI dependency injection
│   ├── exceptions.py       ← Custom error classes
│   ├── middlewares.py      ← Request middleware
│   ├── gradio_app.py       ← Gradio chat interface
│   ├── models/             ← SQLAlchemy ORM models
│   ├── schemas/            ← Pydantic request/response schemas
│   ├── routers/            ← FastAPI route handlers
│   ├── services/           ← Business logic
│   ├── repositories/       ← Database query layer
│   └── db/                 ← Alembic migrations
├── airflow/dags/           ← Airflow DAGs for data ingestion
├── notebooks/              ← Jupyter experiments
├── tests/                  ← Test suite
├── progress/               ← Daily learning summaries
├── compose.yml             ← Docker Compose
├── Dockerfile              ← App container
├── pyproject.toml          ← Dependencies (uv)
├── .env.example            ← Environment variables template
├── LEARNING_LOG.md         ← Daily learning journal
└── CONCEPT_NOTES.md        ← Concepts explained in own words
```

---

## Setup

### Prerequisites
- Python 3.12+
- Docker Desktop
- uv package manager (`pip install uv`)
- Ollama (for local LLM)

### Quick Start

```bash
# 1. Clone
git clone https://github.com/YOUR_USERNAME/production-agentic-rag.git
cd production-agentic-rag

# 2. Setup environment
cp .env.example .env
# Fill in your API keys in .env

# 3. Install Python dependencies
uv sync

# 4. Start infrastructure
docker compose up -d

# 5. Run the API
uv run uvicorn src.main:app --reload

# 6. Check health
curl http://localhost:8000/health
```

---

## Learning Journey

This project was built over 5 days as a structured learning exercise.
See [LEARNING_LOG.md](LEARNING_LOG.md) for the daily journal.
See [CONCEPT_NOTES.md](CONCEPT_NOTES.md) for concept explanations.

| Day | What Was Built |
|-----|---------------|
| Day 1 | Infrastructure, Docker, FastAPI skeleton |
| Day 2 | Airflow pipeline, arXiv fetcher, Docling parser |
| Day 3 | Jina embeddings, OpenSearch, Hybrid Search + RRF |
| Day 4 | LangGraph agentic layer, Ollama LLM, FastAPI endpoints |
| Day 5 | Langfuse observability, Redis cache, Telegram bot, Gradio UI |

---

## License

MIT
