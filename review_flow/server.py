from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from review_flow.db.database import get_database_session
from review_flow.schemas.review_schema import ReviewCreate, ReviewResponse
from review_flow.services.review_service import ReviewService
from review_flow.src.logger import get_logger


app = FastAPI()
logger = get_logger(__name__)


@app.post("/reviews", response_model=ReviewResponse)
def create_review(review: ReviewCreate, db: Session = Depends(get_database_session)):
    logger.info("Creating a new review")
    return ReviewService.create_review(db, review)


@app.get("/reviews", response_model=list[ReviewResponse])
def get_reviews(db: Session = Depends(get_database_session)):
    logger.info("Fetching all reviews")
    return ReviewService.get_reviews(db)


@app.get("/reviews/{review_id}", response_model=ReviewResponse)
def get_review(review_id: int, db: Session = Depends(get_database_session)):
    logger.info(f"Fetching review with ID {review_id}")
    review = ReviewService.get_review_by_id(db, review_id)

    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    return review


@app.delete("/reviews/{review_id}")
def delete_review(review_id: int, db: Session = Depends(get_database_session)):
    logger.info(f"Deleting review with ID {review_id}")
    review = ReviewService.delete_review(db, review_id)

    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    return {"message": "Review deleted successfully"}
