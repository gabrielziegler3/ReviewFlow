# **ReviewFlow**

## **📌 Description**
ReviewFlow is a **FastAPI-based microservice** designed to collect and analyze movie reviews.
It provides **CRUD operations** for storing and retrieving reviews, along with a **sentiment analysis endpoint (pending implementation)**.

The service is built using:

✅ **FastAPI** – High-performance web framework
✅ **PostgreSQL** – Database for storing reviews
✅ **SQLAlchemy** – ORM for database interactions
✅ **Docker** – Containerized deployment
✅ **PyTorch** – Fine-tuning DistilBERT for sentiment analysis

---

## **🚀 How to Run the Project**
### **🔹 1. Clone the Repository**
```sh
git clone <repository-url>
cd ReviewFlow
```

### **🔹 2. Build and Run Using Docker**
Ensure **Docker** and **Docker Compose** are installed.
To start the database and API:
```sh
docker compose up --build -d
```
To stop the services:
```sh
docker compose down -v
```

### **🔹 3. Check Logs (Optional)**
```sh
docker compose logs -f api
```

---

## Download dataset from Kaggle

[IMDB Dataset of 50K Movie Reviews]
(https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

## Download the fine-tuned model

[DistilBERT Fine-Tuned Model](https://drive.google.com/drive/folders/1OUxtGb-9blfxzkOPjAy2uasbOJCX9vvC?usp=sharing).
Make sure the model is in the root directory of the project.

---

## **🌍 API Endpoints**
### **1️⃣ Create a Review**
```sh
curl -X POST "http://localhost:7000/reviews" \
     -H "Content-Type: application/json" \
     -d '{
           "text": "An amazing movie with great performances!",
           "sentiment": "positive"
         }'
```

**Response:**
```json
{
    "id": 1,
    "text": "An amazing movie with great performances!",
    "sentiment": "positive"
}
```

---

### **2️⃣ Get All Reviews**
```sh
curl -X GET "http://localhost:7000/reviews"
```

**Response:**
```json
[
    {
        "id": 1,
        "text": "An amazing movie with great performances!",
        "sentiment": "positive"
    }
]
```

---

### **3️⃣ Get a Review by ID**
```sh
curl -X GET "http://localhost:7000/reviews/1"
```

**Response:**
```json
{
    "id": 1,
    "text": "An amazing movie with great performances!",
    "sentiment": "positive"
}
```

---

### **4️⃣ Delete a Review**
```sh
curl -X DELETE "http://localhost:7000/reviews/1"
```

**Response:**
```json
{
    "message": "Review deleted successfully"
}
```

---

### **5️⃣ Analyze the Sentiment of aReviews in Batch**

```sh
curl -X POST "http://localhost:7000/analyze" \
     -H "Content-Type: application/json" \
     -d '{
           "texts": [
             "I love this movie, it was amazing!",
             "This film was terrible, I hated it."
           ]
         }'
```

**Response:**

```json
[
  {
    "sentiment": "positive",
    "confidence": 0.9926753640174866
  },
  {
    "sentiment": "negative",
    "confidence": 0.9990241527557373
  }
]
```

### Future Improvements


# 1️⃣ Backend & API Improvements

- Tests: as the project grows, unit tests and integration tests would be crucial to ensure the reliability of the service.
- Pagination: as the database grows, pagination would be necessary to limit the number of reviews returned in a single request.
- Rate Limiting & Authentication: Secure API access and prevent abuse/DDoS attacks.
- Database Migrations: use a tool like `Alembic` to manage database schema changes.

# 2️⃣ Sentiment Analysis Improvements

- Support More Sentiment Classes: Expand beyond positive/negative to include neutral.
- Incorporate other datasets and sources. Twitter, Reddit, etc.
- Deploy model as a separate service for scalability. This way, the API can scale independently of the sentiment analysis service.
- Optimize inference speed: convert model to ONNX format and use quantization for faster CPU predictions.

# 3️⃣ Deployment & Scalability

- CI/CD Pipeline: automate testing and deployment using GitHub Actions. Here we could test the docker build, unit tests, and deploy to a staging environment.
- Deploy to cloud:
Here, we'd need to specify further the requirements for the application.
If we wanted this service to have a fast response time, we could have something similar to:
    - API Gateway: to manage the API requests and route them to the appropriate service.
    - Load Balancer: to distribute the incoming traffic across multiple instances of the service.
    - Auto-Scaling: to automatically adjust the servers serving the model based on the incoming traffic.
    - Caching: cache most frequent requests to reduce the load on the database, if this is something that can be seen in the distribution of the requests.

If instead, this could be an asynchronous operation that processes batches of reviews, we could have something similar to:
    - Message Queue: to manage the requests and responses to the service.
    - Worker Service: to process the requests in the queue.

- Monitoring: to monitor the performance of the service and the infrastructure.
- Monitoring: monitor drifts in the requests and responses to the model trying to detect if the model is degrading in performance.
