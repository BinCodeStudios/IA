from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes para pruebas; restringe en producción
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Modelo para validar el cuerpo de las peticiones PUT
class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 100

# Endpoint GET para verificar el estado
@app.get("/status")
async def get_status():
    return {"status": "API running", "model": "Mock IA"}

# Endpoint GET para generar texto (mock)
@app.get("/generate/{prompt}")
async def get_generate(prompt: str):
    try:
        # Simulamos una respuesta porque no hay modelo real
        mock_response = {
            "choices": [{"text": f"Respuesta simulada para: {prompt}"}]
        }
        return mock_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint PUT para enviar un prompt (mock)
@app.put("/generate")
async def put_generate(request: PromptRequest):
    try:
        # Simulamos una respuesta
        mock_response = {
            "choices": [{"text": f"Respuesta simulada para: {request.prompt}"}],
            "max_tokens": request.max_tokens
        }
        return mock_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
