from fastapi import APIRouter, Request
from pydantic import BaseModel
from .logger import log_interaction
from .status import get_status

router = APIRouter()

class GenerateRequest(BaseModel):
    prompt: str

class GenerateResponse(BaseModel):
    response: str

@router.post("/generate", response_model=GenerateResponse)
async def generate(request: Request, body: GenerateRequest):
    # Stubbed response
    response_data = {"response": "I'm a local AI model, running offline!"}
    # Log the interaction
    log_interaction(body.dict(), response_data)
    return response_data

@router.get("/status")
async def status():
    return get_status()