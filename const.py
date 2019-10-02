import os
import numpy as np

def wpmtime(t, wpm):
    return t * (60.0 / (50.0 * wpm))

def get_note(freq, seconds):
    return np.sin(freq * np.linspace(0, seconds, seconds * SAMPLING, False) * 2 * np.pi)

PITCH = 700 if 'PITCH' not in os.environ else int(os.environ['PITCH'])
WPM = 20 if 'WPM' not in os.environ else int(os.environ['WPM'])
FARNSWORTH = None if 'FARNSWORTH' not in os.environ else int(os.environ['FARNSWORTH'])
SAMPLING = 8000


DIT = get_note(PITCH, wpmtime(1, WPM))
DAH = get_note(PITCH, wpmtime(3, WPM))
DOT_SPACE = get_note(0, wpmtime(1, WPM))
LETTER_SPACE = get_note(0, wpmtime(3, FARNSWORTH or WPM))
WORD_SPACE = wpmtime(7, FARNSWORTH or WPM)
