FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Run Alembic migrations before starting the API
CMD ["bash", "-c", "alembic upgrade head && uvicorn review_flow.server:app --host 0.0.0.0 --port 7000"]

