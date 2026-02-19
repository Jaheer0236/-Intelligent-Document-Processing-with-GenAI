# ============================================
# processors/text_processor.py
# Extract text from TXT and CSV files
# ============================================

import pandas as pd


def extract_text_from_txt(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read().strip()
        return content if content else "[Empty text file]"
    except Exception as e:
        return f"[ERROR reading text file: {str(e)}]"


def extract_text_from_csv(file_path: str) -> str:
    try:
        df = pd.read_csv(file_path)
        return df.to_string(index=False)
    except Exception as e:
        return f"[ERROR reading CSV file: {str(e)}]"