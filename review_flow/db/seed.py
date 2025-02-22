import csv

from review_flow.db.database import get_database_session
from review_flow.db.models import Review
from review_flow.src.constants import DATASET_FILEPATH
from review_flow.src.logger import get_logger


logger = get_logger(__file__)


def populate_db():
    """
    Populate table `Review` with data from the dataset file.
    """
    db = get_database_session()

    if db.query(Review).first() is not None:
        logger.info("Table 'Review' is already populated")
        return

    logger.info(f"Populating database with data from dataset file: {DATASET_FILEPATH}")
    try:
        with open(DATASET_FILEPATH, encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip header
            for row in reader:
                review_text, sentiment = row
                review = Review(text=review_text, sentiment=sentiment)
                db.add(review)
            db.commit()
    except Exception as e:
        logger.error(f"Error populating database: {e}")
        logger.debug(e, exc_info=True)
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    populate_db()
