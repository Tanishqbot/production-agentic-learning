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
**Date:** _Not started yet_
**Status:** ⏳ Pending

### What I Built
- [ ] Project directory structure
- [ ] `.gitignore`, `README.md`, `LEARNING_LOG.md`
- [ ] `pyproject.toml` with uv
- [ ] `src/config.py` — pydantic-settings
- [ ] `src/database.py` — SQLAlchemy engine
- [ ] `src/main.py` — FastAPI app + health endpoint
- [ ] `compose.yml` — Docker Compose
- [ ] First Alembic migration

### Concepts I Understood Today
_Fill in after session_

### Things That Confused Me
_Fill in after session_

### Questions for Next Session
_Fill in after session_

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
- **Project started:** _TBD_
- **Last session:** _TBD_
- **Next session goal:** Day 1 — Set up infrastructure
- **Blockers:** Need to install Docker Desktop
