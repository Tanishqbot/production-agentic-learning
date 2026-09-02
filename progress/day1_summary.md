# Day 1 Progress

**Date:** _Not started yet_
**Status:** ? Pending

## Summary

_Fill in after session_

## What I wrote today

1.  In config.py file:
    I created fields in the config file which is used for type annotations and data validation.
    The values are loaded from the env file automatically and if any error occurs, it will fall back to the default value given in the argument.
    Doing it with the help of pydantic_settings module while inhereting from base settings class.
2.  In database.py file:
    I created the sqlalchemy engine which is used to connect to the databases. It handles all the different type of dialects. So no need to connect manually.
    getting all the variables required from the settings instance using f string in the config file which is getting it from the env file.
    The echo command records all the logs.
    instantiating the declaritive base class. Any python class inherting the base class will automatically be able to map with the database table.
    Here’s your explanation reshaped into a smooth, sequence‑wise paragraph:

            `sessionmaker` is essentially a factory that produces `Session` objects bound to your database engine. A `Session` acts as your workspace for interacting with the database, where you can add, update, delete, or query objects. When you make changes—such as calling `session.add()` or modifying ORM objects—those changes are staged in memory inside the session’s identity map. Flushing is the process of translating these staged changes into SQL and sending them to the database. If `autoflush=True`, this happens automatically before queries; if `autoflush=False`, you must explicitly call `session.flush()`. Flushing doesn’t clear memory—it simply synchronizes the in‑memory state with the database while keeping the objects tracked. Committing finalizes the transaction: it flushes any pending changes and then makes them permanent in the database. In short, flush pushes SQL to the database but doesn’t finalize, while commit both flushes and ends the transaction. You can think of it like writing a draft: the session is your notebook, flush is saving the draft to disk, and commit is publishing it permanently.

3.  In the main.py file:
    Why FastAPI(title=..., description=..., version=...)?
    FastAPI uses these to auto-generate your API documentation page at /docs. When you visit http://localhost:8000/docs, you'll see a beautiful interactive UI (called Swagger UI) that shows all your endpoints, and it uses the title/description/version you set here. This is one of FastAPI's biggest productivity advantages — free docs with zero extra work.

Why @app.get("/health")? What is a decorator?
A decorator is a Python feature that wraps a function and adds behaviour to it. The @ syntax is shorthand for:

`python`

````@app.get("/health")
async def health_check(): ...
# Same as:
async def health_check(): ...
health_check = app.get("/health")(health_check)```

When you write `@app.get("/health")`, FastAPI registers health_check as the function to call whenever someone makes a GET request to /health. No extra wiring needed.

Why does a health endpoint matter in production?
In production, your app runs on a server. Docker, Kubernetes, and load balancers periodically hit GET /health to check the app is alive. If it returns anything other than 200 OK, they automatically restart the container or route traffic elsewhere. It seems simple but it's critical infrastructure.

Why async def vs def?
            |def                                   |	async def                                          |
|Blocking?	|Yes — pauses everything while waiting |No — yields control, handles other requests
|Use when	| CPU-bound                            | no waiting	I/O-bound (DB calls, API calls, file reads)
|FastAPI	|Works, but inefficient	               | Preferred for all route handlers


## Key takeaways
_Fill in after session_

````
