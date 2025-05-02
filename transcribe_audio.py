# ------------------------------------------------------------------------
# STEP 2 ‑ TRANSCRIPTION
# Turn the extracted English audio into raw English text via Deepgram.
def transcribe_audio(audio_path):
    """
    Deepgram‑only transcription (no LLM polishing).
    """
    async def _transcribe():
        dg_client = Deepgram(DEEPGRAM_API_KEY)
        with open(audio_path, "rb") as audio:
            source = {"buffer": audio, "mimetype": "audio/wav"}

            response = await dg_client.transcription.prerecorded(
                source, {"punctuate": True, "language": "en"}
            )
            transcript = response["results"]["channels"][0]["alternatives"][0]["transcript"]
            print("[INFO] Raw transcription:", transcript)
            return transcript

    return asyncio.get_event_loop().run_until_complete(_transcribe())
