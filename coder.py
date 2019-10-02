import time
import operator
import functools
from const import DOT_SPACE, LETTER_SPACE, WORD_SPACE, WPM, FARNSWORTH
from output import play_notes


def insert_spaces(notes, space):
    for i in range(len(notes)):
        notes.insert(i*2, space)
    return notes

def get_letter(letter, code):
    return insert_spaces(code[letter].copy(), DOT_SPACE)

def get_word(word, code):
    notes = [get_letter(letter, code) for letter in list(word)]
    return insert_spaces(notes, LETTER_SPACE)

def play_string(string, code):
    for word in string.split(' '):
        play_notes(get_word(word, code))
        time.sleep(WORD_SPACE)


