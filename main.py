# ============================================
# main.py - Intelligent Document Processor
# Author: Jaheer Khan
# ============================================

import os
import datetime
from config import SUPPORTED_EXTENSIONS, SAMPLE_DOCS_DIR

from processors.pdf_processor  import extract_text_from_pdf
from processors.word_processor import extract_text_from_word, extract_text_from_excel
from processors.text_processor import extract_text_from_txt, extract_text_from_csv

from ai_engine import summarize_document, extract_key_information, classify_document, analyze_tone
from output_generator import save_json, save_text_report, save_excel


def extract_text(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_word(file_path)
    elif ext in [".xlsx", ".xls"]:
        return extract_text_from_excel(file_path)
    elif ext == ".txt":
        return extract_text_from_txt(file_path)
    elif ext == ".csv":
        return extract_text_from_csv(file_path)
    else:
        return f"[Unsupported file type: {ext}]"


def process_document(file_path: str) -> dict:
    file_name = os.path.basename(file_path)
    file_ext  = os.path.splitext(file_name)[1].lower()
    file_size = f"{os.path.getsize(file_path) / 1024:.2f} KB"

    print(f"\n{'='*60}")
    print(f"  📄 Processing: {file_name}")
    print(f"{'='*60}")

    print("  🔍 Extracting text...")
    text = extract_text(file_path)

    if text.startswith("[ERROR") or text.startswith("[Unsupported"):
        print(f"  ❌ {text}")
        return {}

    print(f"  ✅ Extracted {len(text)} characters")

    print("  🤖 Summarizing document...")
    summary = summarize_document(text)

    print("  🤖 Extracting key information...")
    extracted_info = extract_key_information(text)

    print("  🤖 Classifying document...")
    category = classify_document(text)

    print("  🤖 Analyzing tone...")
    tone = analyze_tone(text)

    result = {
        "file_name"     : file_name,
        "file_type"     : file_ext,
        "file_size"     : file_size,
        "processed_at"  : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "summary"       : summary,
        "extracted_info": extracted_info,
        "category"      : category,
        "tone"          : tone,
    }

    base_name = os.path.splitext(file_name)[0]
    print("  💾 Saving outputs...")
    save_json(result, base_name)
    save_text_report(result, base_name)

    return result


def process_all_documents(folder_path: str) -> list:
    all_results = []

    files = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if os.path.splitext(f)[1].lower() in SUPPORTED_EXTENSIONS
    ]

    if not files:
        print(f"\n⚠️  No supported files found in '{folder_path}'")
        print(f"   Supported types: {', '.join(SUPPORTED_EXTENSIONS)}")
        return []

    print(f"\n📁 Found {len(files)} document(s) to process...")

    for file_path in files:
        result = process_document(file_path)
        if result:
            all_results.append(result)

    if all_results:
        print(f"\n📊 Generating combined Excel report...")
        save_excel(all_results, "all_documents_summary")

    return all_results


def main():
    print("\n" + "="*60)
    print("   🧠 INTELLIGENT DOCUMENT PROCESSOR")
    print("   Powered by Groq (LLaMA) | By Jaheer Khan")
    print("="*60)

    os.makedirs(SAMPLE_DOCS_DIR, exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    print("\nChoose mode:")
    print("  1. Process a single file")
    print("  2. Process all files in 'sample_docs' folder")

    choice = input("\nEnter choice (1 or 2): ").strip()

    if choice == "1":
        file_path = input("Enter full path to the document: ").strip()
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            return
        result = process_document(file_path)
        if result:
            save_excel([result], os.path.splitext(result["file_name"])[0])
            print("\n✅ Done! Check the 'outputs' folder for your results.")

    elif choice == "2":
        results = process_all_documents(SAMPLE_DOCS_DIR)
        if results:
            print(f"\n✅ Done! Processed {len(results)} document(s).")
            print("   📁 Check the 'outputs' folder for all results.")
        else:
            print("\n⚠️  No documents were processed.")
    else:
        print("❌ Invalid choice. Please run again and enter 1 or 2.")


if __name__ == "__main__":
    main()