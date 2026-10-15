import argparse
import pandas as pd
from pathlib import Path
from .classifier import KeywordClassifier
from .tagger import DataTagger

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Classify and tag rows of a CSV file based on keyword rules."
    )
    parser.add_argument("--input", required=True, help="Path to input CSV file.")
    parser.add_argument("--output", required=True, help="Path where the tagged CSV will be saved.")
    parser.add_argument(
        "--config",
        default=str(Path(__file__).resolve().parents[1] / "config.yaml"),
        help="Path to classification config YAML.",
    )
    parser.add_argument(
        "--text-column",
        default="text",
        help="Name of the column that contains text to classify.",
    )
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    # Load data
    df = pd.read_csv(args.input)
    # Initialise classifier and tagger
    classifier = KeywordClassifier(args.config)
    tagger = DataTagger(classifier, text_column=args.text_column)
    # Tag data
    tagged_df = tagger.tag_dataframe(df)
    # Save result
    tagged_df.to_csv(args.output, index=False)
    print(f"Tagged data written to {args.output}")

if __name__ == "__main__":
    main()
