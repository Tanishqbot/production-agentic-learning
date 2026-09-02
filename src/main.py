from fastapi import FastAPI

# creating the FastAPI instance
# Entry point for the web api
app = FastAPI(
    title = "Research Paper Curator",
    description = ("research assistant system that automatically fetches academic papers, "
                  "understands their content, and answers your research questions "
                  "using advanced RAG techniques."),
    version = "1.0.0"
)

# to check the health
# using async as there are mutliple connections and the request should run parallely
@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "production-agentic-rag"}

#creating a root endpoint
@app.get("/")
async def read_root():
        return {"app": "My FastAPI Service",
            "version": "1.0.0",
            "status": "running",
            "docs": "Visit /docs for API documentation"
            }
