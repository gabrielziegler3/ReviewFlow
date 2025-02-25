import torch
import torch.nn.functional as F

from tqdm import tqdm
from review_flow.src.logger import get_logger
from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast
from review_flow.src.constants import REVIEW_SENTIMENT_ANALYZER_MODEL_PATH


logger = get_logger(__file__)


class ReviewSentimentAnalyzerService:
    """
    A class for loading a fine-tuned DistilBERT model and performing sentiment analysis
    on movies reviews for binary classification: positive or negative.

    Attributes:
        model_path (str): Path to the saved model directory.
        model (DistilBertForSequenceClassification): The loaded DistilBERT model.
        tokenizer (DistilBertTokenizerFast): The tokenizer for processing input text.
        device (torch.device): The device (CPU or GPU) where the model runs.
    """

    def __init__(self, model_path: str = REVIEW_SENTIMENT_ANALYZER_MODEL_PATH) -> None:
        """
        Initializes the SentimentAnalyzer class by loading the model and tokenizer.

        Args:
            model_path (str): The path to the directory containing the model and tokenizer.
        """
        logger.debug(f"Loading ReviewSentimentAnalyzer model from: {model_path}")
        self.model_path = model_path
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        logger.debug(f"Using device: {self.device}")

        # Load model with SafeTensors support
        self.model = DistilBertForSequenceClassification.from_pretrained(model_path)
        self.tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)

        self.model.to(self.device)
        self.model.eval()

        self.label_map = {0: "negative", 1: "positive"}
        logger.info("SentimentAnalyzer initialized successfully")

    def predict(
        self, texts: list[str], batch_size: int = 32
    ) -> list[tuple[str, float]]:
        """
        Predicts sentiment for a batch of texts in smaller chunks to prevent memory overflow.

        Args:
            texts (list[str]): List of input texts for sentiment analysis.
            batch_size (int): Number of texts to process at a time.

        Returns:
            list[tuple[str, float]]: A list of tuples containing the predicted sentiment
                                     ("positive" or "negative") and confidence score.
        """
        results = []
        num_samples = len(texts)

        for i in tqdm(
            range(0, num_samples, batch_size), desc="Processing batches", unit="batch"
        ):
            batch_texts = texts[i : i + batch_size]

            inputs = self.tokenizer(
                batch_texts, truncation=True, padding=True, return_tensors="pt"
            ).to(self.device)

            # Perform inference
            with torch.no_grad():
                logits = self.model(**inputs).logits

            probs = F.softmax(logits, dim=-1)
            confidence, predicted_classes = torch.max(probs, dim=-1)

            batch_results = [
                (self.label_map[predicted_classes[j].item()], confidence[j].item())
                for j in range(len(batch_texts))
            ]
            results.extend(batch_results)

        return results

    def clear(self) -> None:
        """
        Clears the model and tokenizer from memory.
        """
        del self.model
        del self.tokenizer
        torch.cuda.empty_cache()
        logger.debug("Model and tokenizer cleared from memory")
