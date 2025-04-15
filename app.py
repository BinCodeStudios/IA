from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# Modelo para validar el cuerpo de las peticiones PUT
class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 100

# Endpoint GET para verificar el estado
@app.get("/status")
async def get_status():
    return {"status": "API running", "model": "Gemma 3"}

# Endpoint GET para generar texto
@app.get("/generate/{prompt}")
async def get_generate(prompt: str):
    try:
        # Placeholder para el modelo (ajustaremos en Render)
        model_url = "http://localhost:8000/v1/completions"  # Cambiará según el modelo
        payload = {"prompt": prompt, "max_tokens": 100}
        response = requests.post(model_url, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=500, detail="Error al contactar el modelo")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint PUT para enviar un prompt
@app.put("/generate")
async def put_generate(request: PromptRequest):
    try:
        model_url = "http://localhost:8000/v1/completions"
        payload = {"prompt": request.prompt, "max_tokens": request.max_tokens}
        response = requests.post(model_url, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=500, detail="Error al contactar el modelo")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
