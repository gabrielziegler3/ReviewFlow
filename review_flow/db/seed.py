import csv

from review_flow.db.database import database
from review_flow.db.models import Review
from review_flow.src.constants import DATASET_FILEPATH
from review_flow.src.logger import get_logger


logger = get_logger(__file__)


def populate_db():
    """
    Populate table `Review` with data from the dataset file.
    """
    logger.info(f"Populating database with data from dataset file: {DATASET_FILEPATH}")
    db = next(database.get_db())

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
