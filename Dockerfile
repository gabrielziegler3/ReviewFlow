FROM python:3.12

WORKDIR /app

COPY pyproject.toml .

COPY poetry.lock .

COPY . .

RUN pip install --no-cache-dir poetry && poetry install --no-root

CMD ["poetry", "run", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "7000"]

