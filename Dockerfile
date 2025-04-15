# Usa una imagen base ligera
FROM python:3.9-slim

# Configura el directorio de trabajo
WORKDIR /app

# Copia solo los archivos necesarios
COPY requirements.txt .
COPY app.py .

# Instala dependencias del sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libc6-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Instala torch desde la fuente oficial de PyTorch (CPU)
RUN pip install --no-cache-dir torch==2.0.1 --index-url https://download.pytorch.org/whl/cpu

# Instala las demás dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto
EXPOSE 8000

# Comando para iniciar la app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
