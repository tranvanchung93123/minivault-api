from fastapi import FastAPI
from .api import router

app = FastAPI(
    title="MiniVault API",
    description="A lightweight local REST API that simulates a core ModelVault feature.",
    version="1.0.0"
)

app.include_router(router)