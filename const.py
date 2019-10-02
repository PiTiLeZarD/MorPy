import os

DIT = 1
DAH = 3
DOT_SPACE = 1
LETTER_SPACE = DAH
WORD_SPACE = DAH * 2 + DIT
PITCH = 700 if 'PITCH' not in os.environ else int(os.environ['PITCH'])
WPM = 20 if 'WPM' not in os.environ else int(os.environ['WPM'])
FARNSWORTH = None if 'FARNSWORTH' not in os.environ else int(os.environ['FARNSWORTH'])
SAMPLING = 8000