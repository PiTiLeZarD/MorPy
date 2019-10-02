import numpy as np
import simpleaudio as sa
from const import PITCH

def beep(seconds):
    fs = 44100
    t = np.linspace(0, seconds, seconds * fs, False)
    note = np.sin(PITCH * t * 2 * np.pi)
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    audio = audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj.wait_done()