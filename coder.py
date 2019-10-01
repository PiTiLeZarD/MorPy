import time
from const import DOT_SPACE, LETTER_SPACE, WORD_SPACE, WPM
from output import beep

def wpmtime(t):
    return t * (60.0 / (50.0 * WPM))

def play_letter(letter):
    for dot in letter:
        beep(wpmtime(dot))
        time.sleep(wpmtime(DOT_SPACE))
    time.sleep(wpmtime(LETTER_SPACE))

def play_word(word):
    [ play_letter(letter) for letter in word ]
    time.sleep(wpmtime(WORD_SPACE))

def play_string(string, code):
    [play_word([ code[l] for l in word ]) for word in string.split()]