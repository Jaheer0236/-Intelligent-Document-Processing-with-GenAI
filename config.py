# ============================================
# config.py - Configuration Settings
# ============================================

import os

# ----------------------------
# GROQ API Configuration
# ----------------------------
GROQ_API_KEY = "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"  # Replace with your actual Groq API key
GROQ_MODEL = "llama-3.3-70b-versatile"

# ----------------------------
# Supported File Types
# ----------------------------
SUPPORTED_EXTENSIONS = [".pdf", ".docx", ".xlsx", ".xls", ".txt", ".csv"]

# ----------------------------
# Output Settings
# ----------------------------
OUTPUT_DIR = "outputs"
SAMPLE_DOCS_DIR = "sample_docs"

# ----------------------------
# AI Processing Settings
# ----------------------------
MAX_TOKENS = 1024
TEMPERATURE = 0.3

# ----------------------------
# Document Classification Categories
# ----------------------------
DOC_CATEGORIES = [
    "Invoice / Financial Document",
    "Report / Analysis",
    "Manual / Guide",
    "Contract / Legal",
    "Resume / CV",
    "Email / Communication",
    "Research Paper",
    "Other"
]