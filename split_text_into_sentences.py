# UTILITY ‑ SENTENCE SPLITTER
# Shared helper used by the translation & TTS steps.
def split_text_into_sentences(text, language="en"):
    pattern = r"(?<=[.!؟])\s+" if language == "ar" else r"(?<=[.!?])\s+"
    return [s.strip() for s in re.split(pattern, text) if s.strip()]
