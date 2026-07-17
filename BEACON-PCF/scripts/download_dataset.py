"""
BEACON-PCF
Dataset Setup Script

Downloads the Carbon Catalogue dataset from Kaggle.
"""

import json
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

DATASET = "jeannettesavage/the-carbon-catalogue-public-database"

def configure_kaggle():

    username = os.getenv("KAGGLE_USERNAME")
    key = os.getenv("KAGGLE_KEY")

    if not username or not key:
        raise RuntimeError(
            "KAGGLE_USERNAME or KAGGLE_KEY not found.\n"
            "Please add them to your .env file."
        )

def download_dataset():

    configure_kaggle()

    from kaggle.api.kaggle_api_extended import KaggleApi

    api = KaggleApi()
    api.authenticate()

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    api.dataset_download_files(
        DATASET,
        path=DATA_DIR,
        unzip=True,
        quiet=False,
    )


def main():

    if DATA_DIR.exists() and any(DATA_DIR.iterdir()):
        print(" Dataset already exists.")
        return

    download_dataset()
    print(" Dataset downloaded successfully.")


if __name__ == "__main__":
    main()