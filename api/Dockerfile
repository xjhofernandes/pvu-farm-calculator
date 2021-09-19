FROM python:3.8-slim

RUN pip install fastapi uvicorn pandas dnspython

EXPOSE 5000

COPY . /app
WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "${PORT:-5000}"]