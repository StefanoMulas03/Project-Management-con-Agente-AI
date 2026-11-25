from fastapi import FastAPI

app = FastAPI(
    title="Project Management con Agente AI",
    description="API per la gestione di organizzazioni, progetti, attività e documenti, integrate con un agente AI.",
    version="0.1.0"
)


@app.get("/")
def root():
    return {"message": "Project Management API"}