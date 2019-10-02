import numpy as np
import simpleaudio as sa
from const import SAMPLING

def flatten(something):
    if isinstance(something, (list, tuple, set, range)):
        for sub in something:
            yield from flatten(sub)
    else:
        yield something

def play_notes(note_list):
    notes = np.hstack(list(flatten(note_list)))
    audio = notes * (2**15 - 1) / np.max(np.abs(notes))
    audio = audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, SAMPLING)
    play_obj.wait_done()