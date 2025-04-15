# Usa una imagen base ligera
FROM python:3.9-slim

# Configura el directorio de trabajo
WORKDIR /app

# Copia solo los archivos necesarios
COPY requirements.txt .
COPY app.py .

# Instala dependencias del sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Instala dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto
EXPOSE 8000

# Comando para iniciar la app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
