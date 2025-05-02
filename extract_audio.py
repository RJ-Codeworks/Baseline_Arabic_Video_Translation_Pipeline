# ------------------------------------------------------------------------
# STEP 1 ‑ AUDIO EXTRACTION
# Pull the original (English) soundtrack out of the source video.
def extract_audio(video_path, output_audio_path="original_audio.wav"):
    subprocess.call(
        ["ffmpeg", "-y", "-i", video_path, "-vn", "-acodec", "pcm_s16le", output_audio_path]
    )
    return output_audio_path
