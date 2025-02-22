from sqlalchemy.orm import Session
from review_flow.schemas.review_schema import ReviewCreate
from review_flow.repository.review_repository import ReviewRepository


class ReviewService:
    @staticmethod
    def create_review(db: Session, review: ReviewCreate):
        return ReviewRepository.create_review(db, review)

    @staticmethod
    def get_reviews(db: Session):
        return ReviewRepository.get_reviews(db)

    @staticmethod
    def get_review_by_id(db: Session, review_id: int):
        return ReviewRepository.get_review_by_id(db, review_id)

    @staticmethod
    def delete_review(db: Session, review_id: int):
        return ReviewRepository.delete_review(db, review_id)
