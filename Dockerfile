FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash", "-c", "uvicorn review_flow.server:app --host 0.0.0.0 --port 7000"]

