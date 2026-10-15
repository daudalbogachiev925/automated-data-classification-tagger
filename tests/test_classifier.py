import pytest
from src.classifier import KeywordClassifier
from pathlib import Path

@pytest.fixture
def classifier(tmp_path):
    cfg = tmp_path / "cfg.yaml"
    cfg.write_text(
        """
        categories:
          Finance:
            - "invoice"
            - "payment"
          HR:
            - "employee"
            - "salary"
        """
    )
    return KeywordClassifier(str(cfg))

def test_exact_match(classifier):
    assert classifier.classify("Invoice for March") == "Finance"

def test_case_insensitive(classifier):
    assert classifier.classify("PAYMENT received") == "Finance"

def test_no_match(classifier):
    assert classifier.classify("Random text without keywords") is None
