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

