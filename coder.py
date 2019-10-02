import time
from const import DOT_SPACE, LETTER_SPACE, WORD_SPACE, WPM, FARNSWORTH
from output import beep

def wpmtime(t, wpm):
    return t * (60.0 / (50.0 * wpm))

def play_letter(letter):
    for dot in letter:
        beep(wpmtime(dot, WPM))
        time.sleep(wpmtime(DOT_SPACE, WPM))
    time.sleep(wpmtime(LETTER_SPACE, FARNSWORTH or WPM))

def play_word(word):
    [ play_letter(letter) for letter in word ]
    time.sleep(wpmtime(WORD_SPACE, FARNSWORTH or WPM))

def play_string(string, code):
    [play_word([ code[l] for l in word ]) for word in string.split()]