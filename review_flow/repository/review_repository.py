from sqlalchemy.orm import Session
from review_flow.db.models import Review
from review_flow.schemas.review_schema import ReviewCreate


class ReviewRepository:
    @staticmethod
    def create_review(db: Session, review: ReviewCreate):
        db_review = Review(text=review.text, sentiment=review.sentiment)
        db.add(db_review)
        db.commit()
        db.refresh(db_review)
        return db_review

    @staticmethod
    def get_reviews(db: Session):
        return db.query(Review).all()

    @staticmethod
    def get_review_by_id(db: Session, review_id: int):
        return db.query(Review).filter(Review.id == review_id).first()

    @staticmethod
    def delete_review(db: Session, review_id: int):
        db_review = db.query(Review).filter(Review.id == review_id).first()
        if db_review:
            db.delete(db_review)
            db.commit()
        return db_review
