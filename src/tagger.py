from typing import List, Dict
from .classifier import KeywordClassifier
import pandas as pd

class DataTagger:
    """Apply classification tags to a pandas DataFrame.

    The tagger expects a column named ``text`` (or any column you specify) that
    contains the textual content to be classified.
    """

    def __init__(self, classifier: KeywordClassifier, text_column: str = "text"):
        self.classifier = classifier
        self.text_column = text_column

    def tag_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        if self.text_column not in df.columns:
            raise ValueError(f"Column '{self.text_column}' not found in DataFrame")
        # Apply classification row‑wise
        df = df.copy()
        df["category"] = df[self.text_column].apply(self.classifier.classify)
        # Create a tags list – for simplicity we just use the category as a tag
        df["tags"] = df["category"].apply(lambda x: [] if pd.isna(x) else [x])
        return df
