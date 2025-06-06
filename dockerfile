FROM python:3.9-slim-bookworm  
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt  
COPY . .
CMD ["uvicorn", "app.backend.main:app", "--host", "0.0.0.0"]