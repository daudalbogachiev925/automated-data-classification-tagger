import pytest
import pandas as pd
from src.classifier import KeywordClassifier
from src.tagger import DataTagger
from pathlib import Path

@pytest.fixture
def tagger(tmp_path):
    cfg = tmp_path / "cfg.yaml"
    cfg.write_text(
        """
        categories:
          Marketing:
            - "campaign"
            - "lead"
        """
    )
    classifier = KeywordClassifier(str(cfg))
    return DataTagger(classifier, text_column="description")

def test_tagging(tagger):
    df = pd.DataFrame({
        "id": [1, 2, 3],
        "description": [
            "New marketing campaign launched",
            "Lead generation metrics",
            "Unrelated row"
        ]
    })
    result = tagger.tag_dataframe(df)
    # Expected categories
    assert result.loc[0, "category"] == "Marketing"
    assert result.loc[1, "category"] == "Marketing"
    assert pd.isna(result.loc[2, "category"])  # No match
    # Tags column
    assert result.loc[0, "tags"] == ["Marketing"]
    assert result.loc[2, "tags"] == []
