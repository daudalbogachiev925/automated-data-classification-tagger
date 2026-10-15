import yaml
from typing import List, Optional

class KeywordClassifier:
    """Classify a text based on keyword rules defined in a YAML config.

    The config file should have the following structure:
    ```yaml
    categories:
      CategoryName:
        - "keyword1"
        - "keyword2"
    ```
    The first matching category (order of appearance in the file) is returned.
    """

    def __init__(self, config_path: str):
        self.config_path = config_path
        self.categories = self._load_config()

    def _load_config(self) -> List[tuple]:
        with open(self.config_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        # Preserve order of categories as defined in the file
        categories = []
        for cat, keywords in data.get("categories", {}).items():
            # Normalise keywords to lower case for case‑insensitive matching
            lowered = [kw.lower() for kw in keywords]
            categories.append((cat, lowered))
        return categories

    def classify(self, text: str) -> Optional[str]:
        """Return the first matching category for *text* or ``None`` if no match.

        Matching is case‑insensitive and looks for keyword substrings.
        """
        lowered_text = text.lower()
        for category, keywords in self.categories:
            for kw in keywords:
                if kw in lowered_text:
                    return category
        return None
