# ============================================
# processors/pdf_processor.py
# Extract text from PDF files using PyMuPDF
# ============================================

import fitz  # PyMuPDF

def extract_text_from_pdf(file_path: str) -> str:
    try:
        doc = fitz.open(file_path)
        full_text = ""
        
        for page_num, page in enumerate(doc, start=1):
            text = page.get_text()
            full_text += f"\n--- Page {page_num} ---\n{text}"
        
        doc.close()
        
        if not full_text.strip():
            return "[No text found in PDF - might be a scanned image]"
        
        return full_text.strip()
    
    except Exception as e:
        return f"[ERROR reading PDF: {str(e)}]"