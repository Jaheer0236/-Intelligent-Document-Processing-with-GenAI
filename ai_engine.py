# ============================================
# ai_engine.py - Groq AI Processing Engine
# ============================================

from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL, MAX_TOKENS, TEMPERATURE, DOC_CATEGORIES

client = Groq(api_key=GROQ_API_KEY)


def _call_groq(system_prompt: str, user_prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": user_prompt}
            ],
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[AI ERROR: {str(e)}]"


def summarize_document(text: str) -> str:
    system = (
        "You are an expert document analyst. "
        "Read the provided document text and generate a clear, concise summary "
        "in 3-5 sentences. Focus on the main purpose, key points, and conclusions."
    )
    user = f"Please summarize the following document:\n\n{text[:4000]}"
    return _call_groq(system, user)


def extract_key_information(text: str) -> dict:
    system = (
        "You are a data extraction specialist. Extract key information from the document. "
        "Return ONLY a valid JSON object with these exact keys:\n"
        "{\n"
        '  "dates": ["list of dates mentioned"],\n'
        '  "names": ["list of people or organization names"],\n'
        '  "numbers": ["list of important numbers, amounts, percentages"],\n'
        '  "topics": ["list of main topics or keywords"],\n'
        '  "action_items": ["list of any action items, tasks, or recommendations"],\n'
        '  "location": ["list of places mentioned"]\n'
        "}\n"
        "If nothing found for a field, return an empty list. Return ONLY JSON, no extra text."
    )
    user = f"Extract key information from this document:\n\n{text[:4000]}"

    raw = _call_groq(system, user)

    import json
    try:
        clean = raw.strip().strip("```json").strip("```").strip()
        return json.loads(clean)
    except Exception:
        return {
            "dates": [],
            "names": [],
            "numbers": [],
            "topics": [],
            "action_items": [],
            "location": [],
            "raw_extraction": raw
        }


def classify_document(text: str) -> str:
    categories_str = "\n".join(f"- {c}" for c in DOC_CATEGORIES)
    system = (
        "You are a document classification expert. "
        "Classify the document into EXACTLY ONE of the following categories:\n"
        f"{categories_str}\n\n"
        "Reply with ONLY the category name, nothing else."
    )
    user = f"Classify this document:\n\n{text[:2000]}"
    return _call_groq(system, user)


def analyze_tone(text: str) -> str:
    system = (
        "You are a tone analysis expert. Analyze the overall tone of the document. "
        "Respond with ONE of: Formal, Informal, Technical, Positive, Negative, Neutral, Urgent. "
        "Then add a one-line explanation. Format: 'Tone: <tone> - <explanation>'"
    )
    user = f"Analyze the tone of this document:\n\n{text[:2000]}"
    return _call_groq(system, user)