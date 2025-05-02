# ---------- main pipeline  ----------
def translate_video_to_arabic(input_video_path,temp_audio="original_audio.wav",final_output="final_output.mp4",):

    print("[INFO] Extracting audio …")
    extracted_audio = extract_audio(input_video_path, temp_audio)

    print("[INFO] Transcribing English …")
    english_text = transcribe_audio(extracted_audio)

    print("[INFO] Translating to Arabic …")
    arabic_text = translate_text_in_sentences(english_text)
    print("[INFO] Arabic translation:", arabic_text)

    print("[INFO] Synthesizing Arabic speech …")
    arabic_audio = synthesize_speech(arabic_text, speaker_wav=extracted_audio)

    print("[INFO] Running Wav2Lip …")
    lip_synced_video = lip_sync_local(input_video_path, arabic_audio, final_output)

    print(f"\n✅ Done! Final video saved at: {lip_synced_video}")
    return lip_synced_video
