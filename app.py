from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia a dominios específicos en producción
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Cargar el modelo DistilGPT2 para generación de texto
try:
    generator = pipeline("text-generation", model="distilgpt2", device=-1)  # device=-1 para CPU
except Exception as e:
    print(f"Error cargando el modelo: {e}")
    generator = None

# Modelo para validar el cuerpo de las peticiones PUT
class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 50

# Endpoint GET para verificar el estado
@app.get("/status")
async def get_status():
    return {"status": "API running", "model": "DistilGPT2"}

# Endpoint GET para generar texto
@app.get("/generate/{prompt}")
async def get_generate(prompt: str):
    if not generator:
        raise HTTPException(status_code=500, detail="Modelo no disponible")
    try:
        # Generar respuesta con el modelo
        result = generator(prompt, max_length=50, num_return_sequences=1, truncation=True)
        response_text = result[0]["generated_text"]
        return {"choices": [{"text": response_text}]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generando texto: {str(e)}")

# Endpoint PUT para enviar un prompt
@app.put("/generate")
async def put_generate(request: PromptRequest):
    if not generator:
        raise HTTPException(status_code=500, detail="Modelo no disponible")
    try:
        # Generar respuesta con el modelo
        result = generator(request.prompt, max_length=request.max_tokens, num_return_sequences=1, truncation=True)
        response_text = result[0]["generated_text"]
        return {"choices": [{"text": response_text}], "max_tokens": request.max_tokens}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generando texto: {str(e)}")
