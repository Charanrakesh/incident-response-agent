from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.connection import engine, Base
from app.api.incidents import router as incident_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Incident Response Agent",
    description="AI-powered incident management and memory system",
    version="0.1.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    incident_router,
    tags=["Incidents"],
)


@app.get("/")
def root():
    return {
        "message": "Incident Response Agent is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }