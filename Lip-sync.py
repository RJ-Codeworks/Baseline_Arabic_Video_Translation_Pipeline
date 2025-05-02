# STEP 5 ‑ LIP‑SYNC
# Replace the speaker’s mouth movements so they match the new Arabic audio.
def lip_sync_local(video_path, audio_path, output_path="final_output.mp4"):
    inference_script = "/home/eljoe/Wav2Lip/inference.py"
    checkpoint = "/home/eljoe/Wav2Lip/checkpoints/wav2lip_gan.pth"
    subprocess.run(
        [
            "python3",
            inference_script,
            "--checkpoint_path", checkpoint,
            "--face", video_path,
            "--audio", audio_path,
            "--outfile", output_path,
        ],
        check=True,
    )
    return output_path
