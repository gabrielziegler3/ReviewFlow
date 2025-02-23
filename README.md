# **ReviewFlow**

## **📌 Description**
ReviewFlow is a **FastAPI-based microservice** designed to collect and analyze movie reviews.
It provides **CRUD operations** for storing and retrieving reviews, along with a **sentiment analysis endpoint (pending implementation)**.

The service is built using:
✅ **FastAPI** – High-performance web framework
✅ **PostgreSQL** – Database for storing reviews
✅ **SQLAlchemy** – ORM for database interactions
✅ **Docker** – Containerized deployment
✅ **PyTorch (Planned)** – Fine-tuning DistilBERT for sentiment analysis

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

### **5️⃣ UAnalyze the Sentiment of a Review **

```sh
❯ curl -X 'POST' \                                                                                                                        ─╯
  'http://localhost:7000/analyze' \
  -H 'Content-Type: application/json' \
  -d '{"text": "I absolutely loved this movie! The story was fantastic."}'
```

**Response:**

```json
{
    {"sentiment":"positive","confidence":0.9982852339744568}%
}
```

