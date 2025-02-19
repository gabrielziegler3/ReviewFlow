from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to ReviewFlow API"}


# Placeholder for review routes
@app.post("/reviews")
def create_review():
    return {"message": "Review created"}


@app.get("/reviews/{movie_id}")
def get_reviews(movie_id: int):
    return {"message": f"Fetching reviews for movie {movie_id}"}


@app.put("/reviews/{review_id}")
def update_review(review_id: int):
    return {"message": f"Review {review_id} updated"}


@app.delete("/reviews/{review_id}")
def delete_review(review_id: int):
    return {"message": f"Review {review_id} deleted"}


@app.post("/analyze")
def analyze_review():
    return {"message": "Sentiment analysis result"}
