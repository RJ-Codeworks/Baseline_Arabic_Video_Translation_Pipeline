# STEP 4 ‑ ARABIC TTS
# Synthesize Arabic speech (XTTS) from the translated text.
def synthesize_speech(text, speaker_wav, output_audio_path="arabic_audio.wav"):
    with safe_globals([XttsConfig, XttsAudioConfig, BaseDatasetConfig, XttsArgs]):
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False)

    final_audio = AudioSegment.silent(duration=500)
    for idx, sentence in enumerate(split_text_into_sentences(text, language="ar")):
        temp_audio = f"temp_sentence_{idx}.wav"
        tts.tts_to_file(
            text=sentence,
            speaker_wav=speaker_wav,
            language="ar",
            file_path=temp_audio,
        )
        final_audio += AudioSegment.from_wav(temp_audio) + AudioSegment.silent(duration=250)

    final_audio.export(output_audio_path, format="wav")
    return output_audio_path
