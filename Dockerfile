FROM python:3.11-slim

# Imposta la cartella di lavoro nel container
WORKDIR /app

# Copia il file dei requisiti dal tuo PC al container
COPY requirements.txt .

# Installa le librerie (Ollama, Traceloop, ecc.)
RUN pip install --no-cache-dir -r requirements.txt

# Copia il tuo script python
COPY main.py .

# Avvia lo script senza buffering per vedere i log subito
CMD ["python", "-u", "main.py"]
