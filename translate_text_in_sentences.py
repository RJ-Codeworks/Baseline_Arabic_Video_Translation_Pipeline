# STEP 3 ‑ TRANSLATION
# Translate the English transcript sentence‑by‑sentence into Arabic.
def translate_text_in_sentences(text):
    model_name = "Helsinki-NLP/opus-mt-en-ar"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    translated_sentences = []
    for sentence in split_text_into_sentences(text, language="en"):
        encoded = tokenizer(sentence, return_tensors="pt", truncation=True)
        out_max_len = min(2 * encoded.input_ids.shape[1], 512)

        generated = model.generate(
            **encoded, max_length=out_max_len, num_beams=4, early_stopping=True
        )
        translated_sentences.append(tokenizer.decode(generated[0], skip_special_tokens=True))

    return " ".join(translated_sentences)
