FROM python:3.9.1-alpine

WORKDIR /usr/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "run", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "8002"]