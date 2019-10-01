import time
from const import DOT_SPACE, LETTER_SPACE, WORD_SPACE
from output import beep

def play_letter(letter):
    for dot in letter:
        beep(dot / 10)
        time.sleep(DOT_SPACE / 10)
    time.sleep(LETTER_SPACE / 10)

def play_word(word):
    [ play_letter(letter) for letter in word ]
    time.sleep(WORD_SPACE / 10)

def play_string(string, code):
    [play_word([ code[l] for l in word ]) for word in string.split()]