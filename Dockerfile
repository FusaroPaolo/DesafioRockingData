
FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia todos los archivos y carpetas

COPY . .

CMD ["python", "app.py"]

