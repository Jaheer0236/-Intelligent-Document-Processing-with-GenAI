# 🧠 Intelligent Document Processing with GenAI

> AI-powered tool that automatically extracts, summarizes, classifies, and structures key information from any document using LLM APIs.

---

## 📌 Project Overview

This project is an end-to-end intelligent document processing system. It accepts multiple file formats — PDF, Word, Excel, CSV, and plain text — and uses the **Groq API (LLaMA)** to automatically:

- 📝 Summarize the document in 3-5 sentences
- 🔍 Extract key information (dates, names, numbers, topics, action items)
- 🏷️ Classify the document type automatically
- 🎭 Analyze the tone (Formal, Technical, Urgent etc.)
- 📊 Save outputs as Excel, JSON, and Text Report

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| Multi-format support | PDF, Word (.docx), Excel (.xlsx), CSV, Plain Text |
| AI Summarization | Concise 3-5 sentence summary of any document |
| Key Info Extraction | Dates, Names, Numbers, Topics, Locations, Action Items |
| Auto Classification | Categorizes document type using AI |
| Tone Analysis | Detects Formal / Informal / Technical / Urgent tone |
| Excel Report | Styled multi-document summary spreadsheet |
| JSON Output | Structured data for further processing |
| Text Report | Clean readable report with all extracted info |

---

## 🗂️ Project Structure

```
intelligent_doc_processor/
│
├── main.py                    # Entry point
├── config.py                  # API key & settings
├── ai_engine.py               # Groq AI processing (summarize, extract, classify)
├── output_generator.py        # Excel, JSON, Text report generation
├── requirements.txt           # Required libraries
│
├── processors/
│   ├── __init__.py
│   ├── pdf_processor.py       # PDF text extraction (PyMuPDF)
│   ├── word_processor.py      # Word & Excel extraction
│   └── text_processor.py     # TXT & CSV extraction
│
├── sample_docs/               # Drop your documents here
└── outputs/                   # All generated outputs saved here
```

---

## 🚀 Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/intelligent_doc_processor.git
cd intelligent_doc_processor
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Groq API Key
Open `config.py` and replace:
```python
GROQ_API_KEY = "your_groq_api_key_here"
```
Get your free API key from [console.groq.com](https://console.groq.com)

### 5. Add documents
Place any PDF, Word, Excel, CSV, or TXT files into the `sample_docs/` folder.

### 6. Run
```bash
python main.py
```

Choose:
- **1** → Process a single specific file
- **2** → Process all files in `sample_docs/` folder

---

## 📤 Output Files

All outputs are saved in the `/outputs` folder:

| File | Description |
|------|-------------|
| `filename_TIMESTAMP.json` | Structured JSON with all extracted data |
| `filename_TIMESTAMP.txt` | Human-readable text report |
| `all_documents_summary_TIMESTAMP.xlsx` | Combined styled Excel report |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python | Core programming language |
| Groq API (LLaMA 3.3-70b) | AI summarization, extraction, classification |
| PyMuPDF (fitz) | PDF text extraction |
| python-docx | Word document processing |
| pandas + openpyxl | Excel reading & styled output generation |
| JSON | Structured data output |

---

## 💡 Prompt Engineering Techniques Used

- **Role-based prompting** — "You are a document analyst..."
- **Structured output prompting** — Force JSON format responses
- **Token limiting** — First 4000 characters used to avoid overflow
- **Temperature control** — Low temp (0.3) for consistent structured output

---

## 📸 Sample Output

```
📄 FILE NAME     : Ai_Automation.pdf
🏷️  CATEGORY      : Resume / CV
🎭 TONE          : Formal
📝 SUMMARY       : Pinjari Jaheer Khan is a data analyst with strong
                   foundation in AI/ML automation...
📅 Dates         : Oct 2022, May 2026, Dec 2025, Feb 2026
👤 Names         : Pinjari Jaheer Khan, Global Quest Technologies
📌 Topics        : Python, SQL, Power BI, ChatGPT, Power Automate
```

---

## 👤 Author

**Pinjari Jaheer Khan**  
Data Analyst | AI & Automation  
📧 jaheerkhanpinjari@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/pjaheerkhan)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
