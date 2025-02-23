FROM pytorch/pytorch:2.6.0-cuda11.8-cudnn9-devel

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="/app"

CMD ["bash", "-c", "python review_flow/db/seed.py && uvicorn review_flow.server:app --host 0.0.0.0 --port 7000"]

