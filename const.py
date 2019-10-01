import os

DIT = 1
DAH = 3
DOT_SPACE = 1
LETTER_SPACE = DAH
WORD_SPACE = DAH * 2 + DIT
WPM = 20 if 'WPM' not in os.environ else int(os.environ['WPM'])