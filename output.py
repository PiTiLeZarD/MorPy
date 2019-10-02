import numpy as np
import simpleaudio as sa
from const import PITCH, SAMPLING

def get_note(freq, seconds):
    return np.sin(freq * np.linspace(0, seconds, seconds * SAMPLING, False) * 2 * np.pi)

def beep(seconds):
    note = get_note(PITCH, seconds)
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    audio = audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, SAMPLING)
    play_obj.wait_done()