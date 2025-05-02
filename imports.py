import os
os.environ["COQUI_TOS_AGREED"] = "1"          # ✅  Coqui licence acceptance (needed for XTTS)
DEEPGRAM_API_KEY = "c61da52d30cc995538391a3d06bde0dc97fce988"   # ✅  put your Deepgram api key here

# ---------------- CORE LIBS -----------------
import subprocess, re, asyncio, nest_asyncio
nest_asyncio.apply()                          # required if you run inside notebooks

# ------------- AUDIO / VIDEO ---------------
from pydub import AudioSegment                # used by synthesize_speech()
from moviepy.editor import VideoFileClip      # only if you call it elsewhere

# -------------  DEEPGRAM --------------------
from deepgram import Deepgram
deepgram_client = Deepgram(DEEPGRAM_API_KEY)

# -------------  TRANSLATION -----------------
from transformers import MarianMTModel, MarianTokenizer

# -------------  TTS (Coqui XTTS) ------------
import torch
from torch.serialization import safe_globals 
from TTS.api import TTS
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs
from TTS.config.shared_configs import BaseDatasetConfig
# -------------  DEVICE FLAG ----------------
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
